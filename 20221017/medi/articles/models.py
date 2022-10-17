from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/')
    tumbnail = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[Thumbnail(100, 200)],
                                format='png',
                                options={'quality': 80})