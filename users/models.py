from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class User(AbstractUser):
  active_chef = models.BooleanField(default=False,
                                    help_text='True if the user is a chef.')
  profile_pic = models.URLField(blank=True, null=True,
                                help_text='URL pointing to the users profile picture')

  objects = UserManager()

