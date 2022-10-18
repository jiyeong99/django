from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from traitlets import default

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(300,400)],
                                format='jpeg',
                                options={'quality':80})

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=80)
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(300,400)],
                                format='jpeg',
                                options={'quality':80})