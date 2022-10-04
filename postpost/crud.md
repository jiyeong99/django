# setting
1. make project folder postpost
2. `python -m venv venv`
3. `source venv/Scripts/activate`
4. `pip list`
5. `pip install django==3.2.13`
6. `django-admin startproject popo`

# startapp and prepare templates
## app & url
1. where is manage.py
2. `python manage.py startapp articles`
3. add popo.settings INSTALLED_APPS 'articles'
4. add popo.urls urlpatterns <br> `path('articles/', include('articles.urls'))`
5. make file urls.py in app articles
   
    ```python
        from django.urls import path, include
        from . from views
        app_name = 'articles'
        urlpatterns = [
            path('index/', views.index, name='index')
        ]
    ```
## template
6.  make directory postpost/popo/templates and file `base.html`
    ```html
    <--! base.html -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width={device-width}, initial-scale=1.0">
        <!-- import bootstrap -->
        <!-- CSS only -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
        <!-- JavaScript Bundle with Popper -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
        <title>Document</title>
    </head>
    <body>
        {% block content %}

        {% endblock %}
    </body>
    </html>

    ```

7.  add popo.settings TEMPLATES = [`'DIRS': [BASE_DIR/'templates'] `...]
8.  make directory articles/templates/articles
9.  add views.py ` from popo.settings import BASE_DIR `

# CRUD
## make model
### models.py

    ```python
    from django.db import models

    # Create your models here.
    class Article(models.Model):
        title = models.CharField(max_length=20)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    ```
## make articles/forms.py
### forms.py
```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']
```
### migrate : generate table
```bash
python manage.py makemigration
python manage.py migrate
```
## index(READ)
### articles/urls.py

    ```python
    from django.urls import path, include
    from . import views

    app_name = 'articles'
    urlpatterns = [
        path('', views.index, name='index'),
    ]
    ```
### views.py

    ```python
    from django.shortcuts import redirect, render
    from .models import Article
    from .forms import Article, ArticleForm
    from popo.settings import BASE_DIR

    # Create your views here.
    def index(request):
        articles = Article.objects.all()
        context = {
            'articles' : articles,
        }
        return render(request, 'articles/index.html', context)
    ```
### articles/templates/articles/index.html

    ```python
    {% extends 'base.html' %}

    {% block content %}

    <h1> This is index.html </h1>

    {% endblock %}
    ```
## CREATE
### articles/urls.py

    ```python
    from django.urls import path, include
    from . import views

    app_name = 'articles'
    urlpatterns = [
        path('', views.index, name='index'),
        path('create/', views.create, name='create'),
        path('new/', views.new, name='new'),
    ]
    ```
### views.py

    ```python
    from django.shortcuts import redirect, render
    from .models import Article
    from .forms import Article, ArticleForm
    from popo.settings import BASE_DIR

    # Create your views here.
    def index(request):
        articles = Article.objects.all()
        context = {
            'articles' : articles,
        }
        return render(request, 'articles/index.html', context)
    
    def create(request):
        if request.method == 'POST':
            # post로 받은 데이터를 db에 저장하기
            article_form = ArticleForm(request.POST)
            if article_form.is_valid():
                article_form.save()
                return redirect('articles:index')
        else:
            article_form = ArticleForm()
        context = {
            'article_form' : article_form,
        }
        return render(request, 'articles/new.html', context)

    def new(request):
        article_form = ArticleForm()
        context = {
            'article_form' : article_form,
        }
        return render(request, 'articles/new.html', context)
    ```
### articles/templates/articles/new.html

    ```python
    {% extends 'base.html' %}

    {% block content %}
    <h1> 글 쓰기 </h1>
    <form action="{% url 'articles:create' %}" method="POST">
        {% csrf_token %}
        {{article_form.as_p}}
        # <label for="title">제목 : </label>
        # <input type="text" name="title" id="title" required>

        # <label for="content">내용 : </label>
        # <textarea name="content" id="content" cols="30" rows="10" required></textarea>
        
        <input type="submit" value="글 쓰기">
    </form>
    {% endblock %}
    ```
### articles/templates/articles/index.html

    ```html
    {% extends 'base.html' %}

    {% block content %}

    <h1> This is index.html </h1>
    <a href="{% url 'articles:create' %}"> 글 쓰기 </a>

    {% for article in articles %}
    <!-- <a href="url 'articels:detail' article.pk">{{ article.title }}</a> -->
    <a href="">{{ article.title }}</a>
    <p>{{ article.created_at }} | {{ article.updated_at }}</p>
    <hr>
    {% endfor %}
    {% endblock %}
    ```
## READ detail
### articles/urls.py
    ```python
    from django.urls import path, include
    from . import views

    app_name = 'articles'
    urlpatterns = [
        path('', views.index, name='index'),
        path('create/', views.create, name='create'),
        path('new/', views.new, name='new'),
        path('<int:pk>/', views.detail, name= 'detail'),
    ]
    ```
### articles/templates/articles
#### detail.html
    ```html
    <h1>{{ article.pk }}번 게시글</h1>
    <p>{{ article.created_at }} | {{ article.updated_at }}</p>
    <p>{{ article.content }} </p>
    <a href="">수정하기</a>
    ```
#### index.html
    ```html
    {% extends 'base.html' %}

    {% block content %}

    <h1> This is index.html </h1>
    <a href="{% url 'articles:create' %}"> 글 쓰기 </a>

    {% for article in articles %}
    <!-- <a href="url 'articels:detail' article.pk">{{ article.title }}</a> -->
    <a href="url 'articles:detail' article.pk">{{ article.title }}</a>
    <p>{{ article.created_at }} | {{ article.updated_at }}</p>
    <hr>
    {% endfor %}
    {% endblock %}
    ```
### views.py

    ```python
    def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = [
        'article' : article,
    ]
    return render(request, 'articles/detail.html', context)
    ```
## UPDATE
### urls.py

    ```py
    from django.urls import path
    from . import views

    app_name = 'articles'
    urlpatterns = [
        path('', views.index, name='index'),
        path('new/', views.new, name='new'),
        path('create/', views.create, name='create'),
        path('<int:pk>/', views.detail, name= 'detail'),
        path('<int:pk>/update/', views.update, name='update'),
    ]
    ```
### templates/article
#### update.html

    ```html
    <h1> 글 수정</h1>
    <form action="" method="POST">
        {% csrf_token %}
        {{ article_form.as_p }}
        <input type="submit" value="수정">
    </form>
    ```
#### detail.html

    ```html
    <h1>{{ article.pk }}번 게시글</h1>
    <p>{{ article.created_at }} | {{ article.updated_at }}</p>
    <p>{{ article.title }} </p>
    <p>{{ article.content }} </p>
    <a href="{% url 'articles:update' article.pk %}">수정하기</a>
    <a href="{% url 'articles:index' %}"> 홈 </a>
    ```
### views.py
    ```python
    def update(request, pk):
        article = Article.objects.get(pk=pk)
        if request.method == 'POST':
            article_form = ArticleForm(request.POST, instance=article)
            if article_form.is_valid():
                article_form.save()
                return redirect('articles:detail', article.pk)
        else :
            article_form = ArticleForm(instance=article)
        context = {
            'article_form' : article_form,
        }
        return render(request, 'articles/update.html', context)
    ```
