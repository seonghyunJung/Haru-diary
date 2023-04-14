from django.shortcuts import render
from .models import Diary


def index(request):
    diary_list = Diary.objects.order_by("-create_date")
    context = {"diary_list": diary_list}
    return render(request, "haru/diary_write.html", context)


def calendar_page(request):
    return render(request, "haru/calendar.html", {})


def graph_page(request):
    return render(request, "haru/statistics.html", {})
