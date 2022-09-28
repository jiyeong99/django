from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Todo(models.Model):
    # django에서 pk는 자동으로 만들어준다.
    content = models.CharField(max_length = 80)
    completed = models.BooleanField(default=False)
    