from django.urls import path
from . import views

# url name space
# url을 이름으로 분류한는 기능
app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create')
]