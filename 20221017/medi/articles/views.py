from django.shortcuts import render
from .models import Articles

def index(request):
    articles = Articles.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)