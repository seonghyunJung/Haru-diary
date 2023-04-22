from django.db import models
from django.contrib.auth.models import User


class Diary(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_diary"
    )
    content = models.TextField()
    create_date = models.DateField()

    # 감정 필드
    neutral = models.FloatField()
    happiness = models.FloatField()
    sadness = models.FloatField()
    angry = models.FloatField()
    disgust = models.FloatField()
    fear = models.FloatField()
    surprise = models.FloatField()
    primary_emotion = models.CharField(max_length=15)
    secondary_emotion = models.CharField(max_length=15)
