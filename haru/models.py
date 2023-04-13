from django.db import models


class Diary(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField()
