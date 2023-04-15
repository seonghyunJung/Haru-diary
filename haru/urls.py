from django.urls import path

from . import views

app_name = "haru"

urlpatterns = [
    path("", views.index, name="index"),
    path("diary/create/", views.diary_create, name="diary_create"),
    path("diary/modify/<int:diary_id>/", views.diary_modify, name="diary_modify"),
    path("calendar/", views.calendar_page, name="calendar_page"),
    path("statistics/", views.graph_page, name="graph_page"),
]
