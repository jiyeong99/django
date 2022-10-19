from multiprocessing import context
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.forms import CustomUserCreationsForm
from django.contrib.auth import get_user_model
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = article.comment_set.all()
    if request.method=='POST':
        comment_form = CommentForm(request.POST,request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect('articles:detail', article_pk)
    else:
        comment_form = CommentForm()
    context = {
        'article' : article,
        'comments' : comments,
        'comment_form' : comment_form,
    }
    return render(request, 'articles/detail.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, '글 작성 완료')
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form' : article_form,
    }
    return render(request, 'articles/create.html', context)

def comment_delete(request, article_pk, cmt_pk): 
    Comment.objects.get(pk=cmt_pk).delete()
    return redirect('articles:detail', article_pk)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user == article.user:
        if request.method == 'POST':
            article_form = ArticleForm(request.POST, request.FILES, instance=article)
            if article_form.is_valid():
                article.save()
                messages.success(request, '글 수정 완료')
                return redirect('articles:detail', article.pk)
        else:
            article_form = ArticleForm(instance=article)
        context = {
            'article_form' : article_form,
        }
        return render(request, 'articles/create.html', context)
    else:
        messages.warning(request, '작성자만 수정할 수 있습니다.')
        return redirect('articles:detail', article.pk)
