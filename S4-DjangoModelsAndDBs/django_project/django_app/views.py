from django.shortcuts import render
from django_app.models import AccessRecord, User

# Create your views here.


def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    context = {'access_records': webpage_list}

    # context = {'message': 'This is a message from views.py!'}
    return render(request, 'index.html', context=context)


def user(request):
    user_list = User.objects.all()
    context = {'users': user_list}
    return render(request, 'user.html', context=context)
