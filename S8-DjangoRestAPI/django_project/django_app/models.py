from django.db import models
from pkg_resources import require

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return '{}, by {}'.format(self.title, self.author)
