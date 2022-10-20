from django.shortcuts import redirect, render
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib import messages

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request,'articles/index.html', context)

def detail(request,article_pk):
    return render(request,'articles/detail.html')

def create(request):
    
    return render(request, 'articles/create.html')

def update(request,article_pk):
    return redirect('articles/detail.html', article_pk)

def delete(request, article_pk):
    return redirect('articles:index')