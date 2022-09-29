from django.shortcuts import render, redirect
from .models import Post

from Todo.settings import BASE_DIR

# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request, 'posts/index.html', context)

def create(request):
    temp = request.GET
    content_ = temp.get('content')
    completed_ = temp.get('completed')
    priority_ = temp.get('priority')
    created_at_ = temp.get('created_at')
    deadline_ = temp.get('deadline')

    Post.objects.create(content=content_, completed=completed_, priority=priority_, created_at=created_at_, deadline=deadline_)

    context = {
        'content' : content_,
        'completed' : completed_,
        'priority' : priority_,
        'created_at' : created_at_,
        'deadline' : deadline_,
    }
    return render(request, 'posts/create.html', context)

def new(request):
    return render(request, 'posts/new.html')
# def create(request):
#     return render(request, 'posts/create.html')
