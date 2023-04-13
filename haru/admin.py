from django.contrib import admin
from .models import Diary


class DiaryAdmin(admin.ModelAdmin):
    search_fields = ["content"]


admin.site.register(Diary, DiaryAdmin)
