from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'text': 'Hello world', 'number': 100}
    return render(request, 'index.html', context)


def help(request):
    return render(request, 'help.html')


def relative(request):
    return render(request, 'relative_url_templates.html')
