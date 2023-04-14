from django.urls import path

from . import views

app_name = "haru"

urlpatterns = [
    path("", views.index, name="index"),
    path("calendar/", views.calendar_page, name="calendar_page"),
    path("statistics/", views.graph_page, name="graph_page"),
]
