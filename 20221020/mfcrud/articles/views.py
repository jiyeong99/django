from django.shortcuts import redirect, render
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request,'articles/index.html', context)

def detail(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    comment = Comment()
    comments = article.comment_set.all()
    context = {
        'article' : article,
        'comments' : comments,
    }
    return render(request,'articles/detail.html', context)

@login_required
def create(request):
    if request.method=='POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, 'create new article!')
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form' : article_form,
    }
    return render(request, 'articles/create.html', context)

def update(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user == article.user:
        if request.method=='POST':
            article_form = ArticleForm(request.POST, request.FILES, instance=article)
            if article_form.is_valid():
                article = article_form.save(commit=False)
                article.user = request.user
                article.save()
                messages.success(request, 'update new article!')
                return redirect('articles:detail', article_pk)
        else:
            article_form = ArticleForm(instance=article)
        context = {
            'article_form' : article_form,
        }
        return render(request, 'articles/create.html', context)
    else:
        messages.warning(request, 'only created user updates article')
        return redirect('articles:detail',article_pk)

def delete(request, article_pk):
    return redirect('articles:index')

# Comment
## Comment.create
def comment_create(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect('articles:detail', article_pk)
    else:
        comment_form = CommentForm()
    context = {
        'comment_form' : comment_form,
    }
    return render(request, 'articles/commentcreate.html', context)

def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
        return redirect('articles:detail', article_pk)
    else:
        messages.warning(request, 'only created user updates article')
        return redirect('articles:detail', article_pk)