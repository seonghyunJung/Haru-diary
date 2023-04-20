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
            author_id=request.user.id, create_date=timezone.now().date()
        )
        return redirect("haru:diary_modify", diary_id=diary.id)
    except:
        return redirect("haru:diary_create", date=timezone.now().date())


@login_required(login_url="account:login")
def diary_create(request, date):
    if request.method == "POST":
        form = DiaryForm(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.author = request.user
            diary.create_date = date
            diary.save()
            # return redirect("haru:index")
    else:
        form = DiaryForm()
    context = {"form": form, "date": date}
    return render(request, "haru/diary_form.html", context)


@login_required(login_url="account:login")
def diary_modify(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    if request.method == "POST":
        form = DiaryForm(request.POST, instance=diary)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.save()
    else:
        form = DiaryForm(instance=diary)
    context = {"form": form, "diary": diary, "date": diary.create_date}
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
    for diary in all_diaries:
        out.append(
            {
                "title": diary.content,
                "id": diary.id,
                "date": diary.create_date,
            }
        )

    return JsonResponse(out, safe=False)


def graph_page(request):
    return render(request, "haru/statistics.html", {})
