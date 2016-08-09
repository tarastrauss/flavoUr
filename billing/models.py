from __future__ import unicode_literals
from users.models import User
from chefs.models import Chef
from django.db import models
from django.core.exceptions import ValidationError

class Address(models.Model):
    '''
    Represents address information for the User or the Chef.
    '''

    user = models.ForeignKey(User, blank=True, null=True,
                             help_text='Foreign key to the user that saved the'
                             ' address.')
    chef = models.ForeignKey(Chef, blank=True, null=True, help_text='Foreign'
                             ' key to the chef that saved the address.')
    title =  models.CharField(blank=True, null=True, max_length=20,
                              help_text='Represents specified name the address.')
    street_address =  models.CharField(max_length=50, help_text='Represents'
                                       'the street address.')
    city =  models.CharField(max_length=30, help_text='Represents'
                             ' specified city.')
    state =  models.CharField(max_length=2, help_text='Represents'
                              ' specified state.')
    zip =  models.CharField(max_length=5, help_text='Represents'
                            ' specified zip code.')
    instructions =  models.CharField(blank=True, null=True, max_length=200,
                                     help_text=' Represents special'
                                     ' instructions for pickup or delivery.')

    def __unicode__(self):

        return self.title or u'Default'

    def save(self, *args, **kwargs):
        '''
        Ensures user or chef is specified before save
        '''

        if not self.user and not self.chef:
            msg = "Address must belong to a user of chef."
            raise ValidationError(msg)
        super(Address, self).save(*args, **kwargs)




