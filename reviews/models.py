from __future__ import unicode_literals
from django.db import models
from chefs.models import Chef
from patrons.models import Patron
from django.db.models import Avg


class Review(models.Model):

  text = models.CharField(max_length=500, blank=True, null=True,
                                 help_text='Patron\'s review of a chef/meal.')
  stars = models.IntegerField(help_text='Patron\'s star rating for a meal')
  patron = models.ForeignKey('patrons.Patron', help_text='Foreign key to the '
                             'patron the review is from.')
  chef = models.ForeignKey('chefs.Chef', help_text='Foreign key to the chef '
                           'that the review is about')

  def __unicode__(self):

    return 'Review of Chef %s' % self.chef.user.first_name

  def save(self, *args, **kwargs):
      '''
      Each time a reivew is made, the average star rating for a chef is
      calculated and the Chef model is updated.
      '''

      super(Review, self).save(*args, **kwargs)
      chef = self.chef
      average = Review.objects.filter(chef=chef).aggregate(Avg('stars'))['stars__avg']
      chef.rating = round(average, 2)
      chef.save()

