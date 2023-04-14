from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from haru.forms import DiaryForm
from .models import Diary


def index(request):
    try:
        diary = Diary.objects.get(create_date=timezone.now().date())
        context = {"diary": diary.content, "today": timezone.now().date()}
        return render(request, "haru/diary_write.html", context)
    except:
        return render(
            request, "haru/diary_write.html", {"today": timezone.now().date()}
        )


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
    context = {"form": form}
    return render(request, "haru/diary_write.html", context)


def calendar_page(request):
    return render(request, "haru/calendar.html", {})


def graph_page(request):
    return render(request, "haru/statistics.html", {})
