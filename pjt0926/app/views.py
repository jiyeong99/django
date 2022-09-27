from multiprocessing import context
from django.shortcuts import render

# Create your views here.


def index(request, _number):
    if _number%2 == 1:
        oe_str = '홀'
    else : 
        oe_str = '짝'
    context = {
        "number": _number,
        "oddeven" : oe_str,
    }
    return render(request, "odev.html",context)

def calc(request, num_1, num_2):
    res1 = num_1 + num_2
    res2 = num_1 - num_2
    res3 = num_1 * num_2
    res4 = num_1 // num_2
    context = {
        "num_1" : num_1,
        "num_2" : num_2,
        "result1" : num_1 + num_2,
        "result2" : num_1 - num_2,
        "result3" : num_1 * num_2,
        "result4" : num_1 // num_2,
    }
    return render(request, "calculater.html",context)
