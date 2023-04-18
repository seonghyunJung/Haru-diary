from django.db import models
from django.contrib.auth.models import User


class Diary(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_diary"
    )
    content = models.TextField()
    create_date = models.DateField()
