from django.shortcuts import render, redirect
from .models import Article
from .forms import Article, ArticleForm
# Create your views here.
# Create your views here.
def index(request):
    # 요청받은 정보를 pk의 내림차순으로 index.html로 전달
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        # post로 받은 데이터를 db에 저장하기
        article_form = ArticleForm(request.POST)
        # 유효성 검사
        if article_form.is_valid():
            # pk를 받기 위한 변수 설정
            article = article_form.save()
            return redirect('articles:detail', article.pk)
    else:
        # get으로 받을 때?
        article_form = ArticleForm()
    context = {
        'article_form' : article_form,
    }
    # new.html로 넘겨
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)
    else :
        article_form = ArticleForm(instance=article)
    context = {
        'article_form' : article_form,
        'article' : article,
    }
    return render(request, 'articles/update.html', context)

def delete(request, pk) :
    Article.objects.get(pk=pk).delete()
    return redirect('articles:index')