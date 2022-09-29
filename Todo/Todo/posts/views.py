from multiprocessing import context
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
    # return render(request, 'posts/create.html', context)
    return redirect('posts:index')

def new(request):
    return render(request, 'posts/new.html')

def edit(request, pk_):
    post = Post.objects.get(pk = pk_)
    context = {
        "post" : post,
    }
    return render(request, 'posts/edit.html', context)

def delete(request, pk) :
    Post.objects.get(id=pk).delete()
    return redirect('posts:index')

def detail(request, pk_):
    post = Post.objects.get(pk = pk_)
    context = {
        'post' : post,
    }
    return render(request, 'posts/detail.html', context)

def update(request, pk_):
    post = Post.objects.get(pk = pk_)

    u_content = request.GET.get('content')
    u_completed = request.GET.get('completed')
    u_priority = request.GET.get('priority')
    u_created_at = request.GET.get('created_at')
    u_deadline = request.GET.get('deadline')

    post.content = u_content
    post.save()
    post.completed = u_completed
    post.save()
    post.priority = u_priority
    post.save()
    post.created_at = u_created_at
    post.save()
    post.deadline = u_deadline
    post.save()
    
    return redirect('posts:detail', post.pk)