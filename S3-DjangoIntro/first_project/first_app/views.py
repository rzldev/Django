from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {'insert_me': 'Hello I\'m from first_app views.py!'}
    return render(request, 'first_app/index.html', context=context)