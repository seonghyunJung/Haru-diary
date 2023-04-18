from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from haru.forms import DiaryForm
from .models import Diary


def index(request):
    try:
        diary = Diary.objects.get(create_date=timezone.now().date())
        return redirect("haru:diary_modify", diary_id=diary.id)
    except:
        return redirect("haru:diary_create")


def diary_create(request):
    if request.method == "POST":
        form = DiaryForm(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.create_date = timezone.now().date()
            diary.save()
            return redirect("haru:index")
    else:
        form = DiaryForm()
    context = {"form": form, "date": timezone.now().date()}
    return render(request, "haru/diary_form.html", context)


def diary_modify(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    if request.method == "POST":
        form = DiaryForm(request.POST, instance=diary)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.save()
            return redirect("haru:index")
    else:
        form = DiaryForm(instance=diary)
    context = {"form": form, "diary": diary, "date": diary.create_date}
    return render(request, "haru/diary_form.html", context)


def diary_delete(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    diary.delete()
    return redirect("haru:index")


def calendar_page(request):
    return render(request, "haru/calendar.html", {})


def graph_page(request):
    return render(request, "haru/statistics.html", {})
