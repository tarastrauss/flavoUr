from __future__ import unicode_literals
from django.db import models
from chefs.models import Chef
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Menu(models.Model):
    '''
    Represents a menu for a Chef.
    '''
    chef = models.ForeignKey(Chef, help_text='Foreign'
                             ' key to the chef that saved the menu.')
    title = models.CharField(max_length=60,
                             help_text='Represents specified name of the menu.')
    delivery = models.BooleanField(default=False,
                                   help_text='True if delivery is specified.')

    def __unicode__(self):

        return self.title

    def to_dict(self):
        '''
        Return a dictionary representation of the menu.

        @return: Dictionary representation of the menu.
        @rtype: dict
        '''

        items = list(Item.objects.filter(menu=self.id).values())
        d = {
            'id': self.id,
            'chef': self.chef,
            'title': self.title,
            'delivery': self.delivery,
            'items': items
        }
        return d


class Item(models.Model):
    '''
    Represents an item on a menu.
    '''
    menu = models.ForeignKey(Menu, help_text='Foreign key to the menu the item'
                             ' belongs to.')
    title = models.CharField(max_length=30, help_text='Represents the name of the item.')
    size = models.CharField(max_length=30, help_text='Represents serving size for the item.')
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                help_text='Represents the price for the item.')
    description = models.CharField(max_length=60,
                                   help_text='A short description, including'
                                   ' ingredints.')

    def __unicode__(self):

        return self.title

