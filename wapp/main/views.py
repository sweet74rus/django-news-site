from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def registration(request):
    return HttpResponse("<h1>Registration...</h1>")
