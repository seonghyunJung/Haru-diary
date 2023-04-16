from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from haru.forms import DiaryForm
from .models import Diary


def index(request):
    try:
        diary = Diary.objects.get(create_date=timezone.now().date())
        context = {"diary": diary, "today": timezone.now().date()}
        # return render(request, "haru/diary_view.html", context)
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
            context = {"diary": diary, "today": timezone.now().date()}
            return render(request, "haru/diary_view.html", context)
    else:
        form = DiaryForm()
    context = {"form": form, "today": timezone.now().date()}
    return render(request, "haru/diary_write.html", context)


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
    context = {"diary": diary, "form": form}
    return render(request, "haru/diary_write.html", context)


def calendar_page(request):
    return render(request, "haru/calendar.html", {})


def graph_page(request):
    return render(request, "haru/statistics.html", {})
