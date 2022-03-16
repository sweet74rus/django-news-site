from django.shortcuts import render
from .models import *

def news_home(request):
    data = {
        'title': 'Новости',
        'news': Articles.objects.order_by('-date')
    }

    return render(request, 'news/news_home.html', data)
