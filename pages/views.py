from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Hello world")
    return render(request, 'pages/index.html')


def about(request):
    # return HttpResponse("<h1>About us</h1>")
    x = -10
    y = 20
    foods = ['tea', 'coffee', 'samosa', 'idli']
    students = {'tom': 80, 'jerry': 45, 'casper': 65,'droopy':35}
    context = {
        'a': x,
        'b': y,
        'foods': foods,
        'students':students
       
    }
    return render(request, 'pages/about.html', context)
def contactus(request):
    # return HttpResponse("Hello world")
    return render(request, 'pages/contactus.html')
