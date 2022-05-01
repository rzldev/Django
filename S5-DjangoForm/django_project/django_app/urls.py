from django.urls import path
from django_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('basic-form/', views.basicForm, name="basic-form"),
    path('model-form/', views.modelForm, name="model-form"),
]
