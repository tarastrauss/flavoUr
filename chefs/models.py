from __future__ import unicode_literals
from users.models import User
from django.db import models

class ChefInfo(models.Model):
    '''
    Represents the Chef Info profile for a User.
    '''

    user_info = models.OneToOneField(User, help_text='Connects user'
                                    'to the ChefInfo class.',
                                    primary_key=True)
    star_rating = models.IntegerField(default=0, help_text='average value of'
                                     'star ratings')

    def __unicode__(self):

        return self.user_info.first_name
