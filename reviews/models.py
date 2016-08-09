from __future__ import unicode_literals
from django.db import models
from chefs.models import Chef
from django.db.models import Avg
from users.models import User


class Review(models.Model):

  text = models.CharField(max_length=500, blank=True, null=True,
                                 help_text='Patron\'s review of a chef/meal.')
  stars = models.IntegerField(help_text='Patron\'s star rating for a meal')
  user = models.ForeignKey(User, help_text='Foreign key to the '
                             'user the review is from.')
  chef = models.ForeignKey(Chef, help_text='Foreign key to the user '
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

