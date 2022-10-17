from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Articles
from .forms import Articles, ArticleForm
from django.contrib import messages
from medi.settings import BASE_DIR, STATIC_URL, MEDIA_URL

def index(request):
    articles = Articles.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article_form.save()
            messages.success(request, '글 작성이 완료되었습니다.')
            return redirect('articles:index')
    else: 
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/create.html', context=context)

def detail(request,pk):
    article = Articles.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request,'articles/detail.html',context)

def delete(request,pk):
    Articles.objects.get(pk=pk).delete()
    return redirect('articles:index')
