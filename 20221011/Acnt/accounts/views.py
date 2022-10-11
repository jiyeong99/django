from multiprocessing import context
from django.shortcuts import redirect, render
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from Acnt.settings import BASE_DIR
# from .models import User

# Create your views here.
def main(request):
    return render(request, 'accounts/main.html')
def index(request):
    view = get_user_model().objects.all()
    context = {
        'view' : view,
    }
    return render(request, 'accounts/index.html',context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)

def detail(request,pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user':user,
    }
    return render(request, 'accounts/detail.html', context)