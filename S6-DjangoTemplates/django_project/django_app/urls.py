from django.urls import path
from django_app import views

# TEMPLATE TAGGING
app_name = 'django_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('help/', views.help, name='help'),
    path('relative/', views.relative, name='relative'),
]
