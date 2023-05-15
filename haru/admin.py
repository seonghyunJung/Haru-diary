from django.contrib import admin
from .models import Diary, Emoji


class DiaryAdmin(admin.ModelAdmin):
    search_fields = ["content"]


class EmojiAdmin(admin.ModelAdmin):
    list_display = "emoji"


admin.site.register(Diary, DiaryAdmin)
admin.site.register(Emoji)
