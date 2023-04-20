from django.urls import path

from . import views

app_name = "haru"

urlpatterns = [
    path("", views.index, name="index"),
    path("diary/create/", views.diary_create, name="diary_create"),
    path("diary/modify/<int:diary_id>/", views.diary_modify, name="diary_modify"),
    path("diary/delete/<int:diary_id>/", views.diary_delete, name="diary_delete"),
    path("calendar/", views.calendar_page, name="calendar_page"),
    path("all_diaries/", views.all_diaries, name="all_diaries"),
    path("statistics/", views.graph_page, name="graph_page"),
]
