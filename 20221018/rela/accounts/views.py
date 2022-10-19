from django.shortcuts import redirect, render
from .forms import CustomUserCreationsForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from articles.forms import ArticleForm
# Create your views here.

def index(request):
    users = get_user_model().objects.all()
    context = {
        'users' : users,
    }
    return render(request, 'accounts/index.html', context)

def signup(request):
    if request.method == 'POST' :
        signup_form = CustomUserCreationsForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        signup_form = CustomUserCreationsForm()
    context = {
        'signup_form' : signup_form,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    articles = ArticleForm()
    context = {
        'user' : user,
        'articles' : user.article_set.all(),
    }
    return render(request, 'accounts/detail.html', context)