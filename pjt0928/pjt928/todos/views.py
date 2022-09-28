from django.shortcuts import render
from .models import Todo

# Create your views here.

def index(request):
    return render(request, 'todos/index.html')

def create(request):
    # content = 템플릿에서 데이터를 get
    content = request.GET.get('content_')
    # print(content)
    Todo.objects.create(content=content)
    return render(request, 'todos/index.html')