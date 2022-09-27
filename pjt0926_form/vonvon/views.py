from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
import random
# Create your views here.
def inputname(request):
    return render(request, 'home.html')
def psl(request):
    past_life = ['의사','왕','왕비','귀족','노예','농부','상인','재봉사','광대','기사','요리사']
    context = {
        'past_life' : random.choice(past_life)
    }
    return render(request, 'pastlife.html', context)