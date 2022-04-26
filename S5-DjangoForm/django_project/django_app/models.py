from turtle import width
from django.db import models
from django.core import validators

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255,
                                validators=[validators.MinLengthValidator(8)])

    def __str__(self):
        return self.username
