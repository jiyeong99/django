from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import is_valid_path
from .models import Article, Comment
from django.views.decorators.http import require_POST, require_safe
from .forms import ArticleForm, CommentForm
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request,'articles/index.html', context)

def detail(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm()
    context = {
        'article' : article,
        'comment_form':comment_form,
        'comments':article.comment_set.all(),
    }
    return render(request, 'articles/detail.html',context)

def create(request):
    if request.method=='POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form' : article_form,
    }
    return render(request, 'articles/form.html', context)

def comment_create(request,article_pk):
    print(request.POST)
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
        context = {
            'content': comment.content,
            'userName': comment.user.userName,
        }
        return JsonResponse(context)
    
def comment_delete(request, article_pk,comment_pk):

    return redirect('article:detail', article_pk)

