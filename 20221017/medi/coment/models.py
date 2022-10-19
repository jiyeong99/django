from django.db import models

# Create your models here.
class Comments(models.Model):
    title = models.TextField()
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)