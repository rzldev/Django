from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete='CASCADE')

    # Additional attributes
    portofolio_site = models.URLField(blank=True)
    profile_pict = models.ImageField(upload_to='profile_picts', blank=True)

    def __str__(self):
        return self.user.username
