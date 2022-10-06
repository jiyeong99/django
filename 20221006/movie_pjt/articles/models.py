from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.TextField()
    summary = models.TextField()
    running_time = models.PositiveIntegerField(default=0)