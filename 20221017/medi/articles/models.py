from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/')
    tumbnail = ProcessedImageField(
        upload_to = 'images/', blank=True,
        processors=[ResizeToFill(1200,960)],
        format='jpeg',
        options={'quality': 80})