from urllib import request
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from movie_pjt.settings import BASE_DIR
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        movie_form = MovieForm(request.POST)
        # 유효성검사
        if movie_form.is_valid():
            # pk 받아서 상세페이지로 넘겨
            movie = movie_form.save()
            return redirect('articles:detail', movie.pk)
    else :
        movie_form = MovieForm()
    context = {
        'movie_form' : movie_form,
    }
    return render(request, 'articles/create.html', context)
def detail(request,pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie,
    }
    return render(request, 'articles/detail.html', context)

def update(request,pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        movie_form = MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie_form.save()
            return redirect('articles:detail', movie.pk)
    else :
        movie_form = MovieForm(instance=movie)
    context = {
        'movie_form' : movie_form,
        'movie' : movie,
    }
    return render(request, 'articles/update.html', context)

def delete(request,pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        movie.delete()
        return redirect('articles:index')
    return render(request,'articles/detail.html')