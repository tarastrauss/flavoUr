from __future__ import unicode_literals
from django.db import models
from users.models import User
from chefs.models import Chef
from menus.models import Menu, Item
from billing.models import Address
from django.db.models import Sum

class Order(models.Model):
    '''
    Represents a created order.
    '''
    customer = models.ForeignKey(User, help_text='Foreign key to the user who'
                                 ' made the order.')
    chef = models.ForeignKey(Chef, help_text='Foreign key to the chef making the'
                            ' meal.')
    customer_address = models.ForeignKey(Address, help_text='Foreign key to the'
                                        ' address information of the customer.')
    item = models.ManyToManyField(Item, help_text='Foreign key to the selected items.')

    total_price = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2,
                                help_text='Represents the price for the item.')

    '''
    Method that automatically updates the total price field based on the items in the order.
    '''
    # @property
    # def total_price(self):
    #     self._total_price = self.item.aggregate(Sum('price'))
    #     return self._total_price
    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)
        self.total_price = self.item.aggregate(Sum('price'))
        self.save()

    def __unicide__(self):

        return 'Order placed by %s to %s' % (self.customer, self.chef)

