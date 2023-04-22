import requests
import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from haru.forms import DiaryForm
from .models import Diary


@login_required(login_url="account:login")
def index(request):
    try:
        diary = Diary.objects.get(
            author_id=request.user.id,
            create_date=timezone.localdate(),
        )
        return redirect("haru:diary_modify", diary_id=diary.id)
    except:
        return redirect("haru:diary_create")


@login_required(login_url="account:login")
def diary_create(request):
    if request.method == "POST":
        form = DiaryForm(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.author = request.user
            diary.create_date = timezone.localdate()

            # request 요청으로 감성분석 모델로부터 감정분석 값 반환
            url = "http://15.165.255.212:50512/Diary"
            obj = {"Text": diary.content}
            emotion = json.loads(requests.post(url, json=obj).text)
            diary.neutral = emotion["neutral"]
            diary.happiness = emotion["happiness"]
            diary.sadness = emotion["sadness"]
            diary.angry = emotion["angry"]
            diary.disgust = emotion["disgust"]
            diary.fear = emotion["fear"]
            diary.surprise = emotion["surprise"]

            # 주요감정 순위별 정렬
            emotion.pop("sentence")
            emotion_rank = sorted(emotion, key=lambda x: emotion[x], reverse=True)
            diary.primary_emotion = (
                emotion_rank[0] if emotion_rank[0] != ("neutral") else emotion_rank[1]
            )
            diary.secondary_emotion = (
                emotion_rank[1] if emotion_rank[1] != ("neutral") else emotion_rank[2]
            )
            diary.save()
            return redirect("haru:diary_modify", diary_id=diary.id)

    else:
        form = DiaryForm()
    context = {"form": form, "date": timezone.localdate()}
    return render(request, "haru/diary_form.html", context)


@login_required(login_url="account:login")
def diary_modify(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    if request.method == "POST":
        form = DiaryForm(request.POST, instance=diary)
        if form.is_valid():
            diary = form.save(commit=False)

            # request 요청으로 감성분석 모델로부터 감정분석 값 반환
            url = "http://15.165.255.212:50512/Diary"
            obj = {"Text": diary.content}
            emotion = json.loads(requests.post(url, json=obj).text)
            diary.neutral = emotion["neutral"]
            diary.happiness = emotion["happiness"]
            diary.sadness = emotion["sadness"]
            diary.angry = emotion["angry"]
            diary.disgust = emotion["disgust"]
            diary.fear = emotion["fear"]
            diary.surprise = emotion["surprise"]

            # 주요감정 순위별 정렬
            emotion.pop("sentence")
            emotion_rank = sorted(emotion, key=lambda x: emotion[x], reverse=True)
            diary.primary_emotion = (
                emotion_rank[0] if emotion_rank[0] != ("neutral") else emotion_rank[1]
            )
            diary.secondary_emotion = (
                emotion_rank[1] if emotion_rank[1] != ("neutral") else emotion_rank[2]
            )
            diary.save()
    else:
        form = DiaryForm(instance=diary)

    emotion_emojis = {
        "happiness": "😊",
        "sadness": "😭",
        "angry": "😡",
        "disgust": "🤮",
        "fear": "😨",
        "surprise": "😳",
    }
    context = {
        "form": form,
        "diary": diary,
        "date": diary.create_date,
        "primary_emotion": emotion_emojis[diary.primary_emotion],
    }
    return render(request, "haru/diary_form.html", context)


@login_required(login_url="account:login")
def diary_delete(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    diary.delete()
    return redirect("haru:calendar_page")


@login_required(login_url="account:login")
def calendar_page(request):
    all_diaries = Diary.objects.filter(author_id=request.user.id)
    context = {"diaries": all_diaries}
    return render(request, "haru/fullcalendar.html", context)


@login_required(login_url="account:login")
def all_diaries(request):
    all_diaries = Diary.objects.filter(author_id=request.user.id)
    out = []
    emotion_emojis = {
        "happiness": "😊",
        "sadness": "😭",
        "angry": "😡",
        "disgust": "🤮",
        "fear": "😨",
        "surprise": "😳",
    }
    for diary in all_diaries:
        out.append(
            {
                # "title": emotion_emojis[diary.primary_emotion],
                "id": diary.id,
                "date": diary.create_date,
                "imageurl": f"../../media/emoji/images/{diary.primary_emotion}.png",
            }
        )

    return JsonResponse(out, safe=False)


def graph_page(request):
    return render(request, "haru/statistics.html", {})
