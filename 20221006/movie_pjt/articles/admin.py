from django.contrib import admin
from .models import Movie
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    fields = ['title','summary','running_time']

admin.site.register(Movie, MovieAdmin)