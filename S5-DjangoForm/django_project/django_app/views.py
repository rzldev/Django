from django.shortcuts import render
from django_app.forms import FormName, UserForm
from django_app.models import User

# Create your views here.


def index(request):
    context = {}

    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form.is_valid())

        user = User(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'])

        context['user'] = user

    return render(request, 'index.html', context=context)


def basicForm(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])

    return render(request, 'basic-form.html', {'form': form})


def modelForm(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            return index(request)

    return render(request, 'model-form.html', {'form': form})
