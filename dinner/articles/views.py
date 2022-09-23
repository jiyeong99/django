from multiprocessing import context
import random
from django.shortcuts import render

# Create your views here.

# define index
def index(request):
    food_names = ['삼겹살', '떡볶이', '카레', '제육볶음', '파스타', '피자', '치킨']
    name = random.choice(food_names)
    food_list = {
    '삼겹살' : 'https://cdn.pixabay.com/photo/2019/11/21/18/28/garlic-ribs-4643142_960_720.jpg',
    '떡볶이' : 'https://media.istockphoto.com/photos/tteokbokki-korean-street-food-picture-id848720654',
    '카레' : 'https://cdn.pixabay.com/photo/2018/11/02/10/50/nutrition-3790031_960_720.jpg',
    '제육볶음' : 'https://media.istockphoto.com/photos/spicy-grilled-pork-belly-with-kochujang-sauce-is-popular-spicy-korean-picture-id1266776544?s=612x612',
    '파스타' : 'https://cdn.pixabay.com/photo/2019/11/14/11/23/pasta-4625962_960_720.jpg',
    '피자' : 'https://cdn.pixabay.com/photo/2020/06/08/16/49/pizza-5275191_960_720.jpg',
    '치킨' : 'https://cdn.pixabay.com/photo/2015/03/11/00/31/chicken-667935_960_720.jpg'
    }

    context = {
        'name' : name,
        'food' : food_list[name]
    }
    return render(request, 'today-dinner.html', context)