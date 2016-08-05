from __future__ import unicode_literals
from users.models import User
from django.db import models
from annoying.fields import AutoOneToOneField

class Patron(models.Model):
    '''
    Represents the Patron Info profile for a User.
    '''

    user = AutoOneToOneField(User, help_text='Automatically connects user '
                                  'to the Patron class when a useris created',
                                  primary_key=True)

    def __unicode__(self):

        return self.user.first_name