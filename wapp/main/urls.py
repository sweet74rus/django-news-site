from django.urls import path
from . import views
from news.views import news_home

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('news', news_home, name='news')
]
