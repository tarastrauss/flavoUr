from __future__ import unicode_literals
from users.models import User
from django.db import models

class Chef(models.Model):
    '''
    Represents the Chef profile for a User.
    '''

    user = models.OneToOneField(User, help_text='Connects user model'
                                    ' to the Chef class.',
                                    primary_key=True)
    rating = models.DecimalField(decimal_places=2, max_digits=3, default=0,
                                      help_text='average value of review stars.')

    def __unicode__(self):

        return self.user.first_name
