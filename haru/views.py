from django.shortcuts import render
from .models import Diary


def index(request):
    diary_list = Diary.objects.order_by("-create_date")
    context = {"diary_list": diary_list}
    return render(request, "haru/statistics.html", context)
