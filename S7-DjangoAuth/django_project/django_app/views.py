from django.shortcuts import render
from django_app.forms import UserForm, UserProfileInfoForm, UserLoginForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        user_profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_profile = user_profile_form.save(commit=False)
            user_profile.user = user

            if 'profile_pict' in request.FILES:
                user_profile.profile_pict = request.FILES['profile_pict']

            user_profile.save()

            registered = True

        else:
            print(user_form.errors, user_profile_form.errors)
            registered = False

    else:
        user_form = UserForm()
        user_profile_form = UserProfileInfoForm()
        registered = False

    context = {
        'registered': registered,
        'user_form': user_form,
        'user_profile_form': user_profile_form
    }

    return render(request, 'registration.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('django_app:index'))

                else:
                    return HttpResponse('ACCOUNT NOT ACTIVE!')
            else:
                print('Someone tried to login and failed!')
                print('username: {}, password: {}'.format(username, password))
                return HttpResponse('INVALID LOGIN DETAILS SUPPLIED!')

    else:
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'login.html', context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('django_app:index'))


@login_required
def special(request):
    return HttpResponse('YOU ARE LOGGED IN, NICE!')
