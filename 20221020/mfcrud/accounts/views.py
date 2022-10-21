from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from articles.models import Article, Comment

# Create your views here.
def index(request):
    users = get_user_model().objects.all()
    context = {
        'users' :users,
    }
    return render(request,'accounts/index.html', context)

def signup(request):
    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            auth_login(request,user)
            return redirect('accounts:index')
    else:
        signup_form = CustomUserCreationForm()
    context = {
        'signup_form' : signup_form,
    }
    return render(request,'accounts/signup.html', context)

def login(request):
    if request.method=='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')

def detail(request, user_pk):
    user_detail = get_user_model().objects.get(pk=user_pk)
    user_articles = user_detail.article_set.all()
    user_comments = user_detail.comment_set.all()

    context = {
        'user_detail' : user_detail,
        'user_articles' : user_articles,
        'user_comments' : user_comments,
    }
    return render(request, 'accounts/detail.html', context)