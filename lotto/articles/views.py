from multiprocessing import context
from django.shortcuts import render
import random
# Create your views here.
def index(request) :
    lotto_list = []
    for _ in range(5):
        number = random.sample(range(1,46), 6)
        lotto_list.append(number)
    context = {
        'number' : lotto_list,
    }
    return render(request, 'index.html', context)