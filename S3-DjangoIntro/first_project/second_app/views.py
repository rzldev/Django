from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('<em>Welcome to Second App</em>')


def help(request):
    context = {'message': 'This is a message from second_app/views.py'}
    return render(request, 'second_app/help.html', context=context)
