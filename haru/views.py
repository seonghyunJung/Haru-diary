import requests
import json

from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
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


@csrf_exempt
@login_required(login_url="account:login")
def graph_page(request):
    if request.method == "POST":
        range = json.loads(request.body)
        diaries = Diary.objects.filter(
            author_id=request.user.id, create_date__range=[range["start"], range["end"]]
        )

        neutral = diaries.filter(neutral__gt=0.0).aggregate(Sum("neutral"))
        neutral = (
            neutral["neutral__sum"] / diaries.count()
            if neutral["neutral__sum"]
            else 0.0
        )
        neutral *= 100

        happiness = diaries.filter(happiness__gt=0.0).aggregate(Sum("happiness"))
        happiness = (
            happiness["happiness__sum"] / diaries.count()
            if happiness["happiness__sum"]
            else 0.0
        )
        happiness *= 100

        sadness = diaries.filter(sadness__gt=0.0).aggregate(Sum("sadness"))
        sadness = (
            sadness["sadness__sum"] / diaries.count()
            if sadness["sadness__sum"]
            else 0.0
        )
        sadness *= 100

        angry = diaries.filter(angry__gt=0.0).aggregate(Sum("angry"))
        angry = angry["angry__sum"] / diaries.count() if angry["angry__sum"] else 0.0
        angry *= 100

        disgust = diaries.filter(disgust__gt=0.0).aggregate(Sum("disgust"))
        disgust = (
            disgust["disgust__sum"] / diaries.count()
            if disgust["disgust__sum"]
            else 0.0
        )
        disgust *= 100

        fear = diaries.filter(fear__gt=0.0).aggregate(Sum("fear"))
        fear = fear["fear__sum"] / diaries.count() if fear["fear__sum"] else 0.0
        fear *= 100

        surprise = diaries.filter(surprise__gt=0.0).aggregate(Sum("surprise"))
        surprise = (
            surprise["surprise__sum"] / diaries.count()
            if surprise["surprise__sum"]
            else 0.0
        )
        surprise *= 100

        statistics = {
            "neutral": neutral,
            "happiness": happiness,
            "sadness": sadness,
            "angry": angry,
            "disgust": disgust,
            "fear": fear,
            "surprise": surprise,
        }

        context = {"statistics": json.dumps(statistics)}
        # print(context)
        # return render(request, "haru/statistics.html", context)
        return JsonResponse(context, status=200)

    else:
        try:
            diary = Diary.objects.get(
                author_id=request.user.id, create_date=timezone.localdate()
            )
            neutral = diary.neutral * 100
            happiness = diary.happiness * 100
            sadness = diary.sadness * 100
            angry = diary.angry * 100
            disgust = diary.disgust * 100
            fear = diary.fear * 100
            surprise = diary.surprise * 100
        except:
            neutral = 0
            happiness = 0
            sadness = 0
            angry = 0
            disgust = 0
            fear = 0
            surprise = 0

        statistics = {
            "neutral": neutral,
            "happiness": happiness,
            "sadness": sadness,
            "angry": angry,
            "disgust": disgust,
            "fear": fear,
            "surprise": surprise,
        }

        context = {"statistics": json.dumps(statistics)}
        return render(request, "haru/statistics.html", context)
