from django.shortcuts import render
from Acnt.settings import BASE_DIR
# Create your views here.
def index(request):
    return render(request,'articles/index.html')