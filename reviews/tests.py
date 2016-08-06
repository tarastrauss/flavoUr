from django.test import TestCase
from users.models import User
from patrons.models import Patron
from chefs.models import Chef
from reviews.models import Review

class ReviewTestCase(TestCase):

    def setUp(self):

        self.test_patron = User.objects.create(username="HungryPerson",
                                               first_name="John")
        self.test_chef = User.objects.create(username="AwesomeChef",
                                             first_name="Jane")
        self.test_chef_profile = Chef.objects.create(user=self.test_chef)

    def test_chef_model(self):
      '''
      Tests creation of the Chef model and links to other models.
      '''

      # Tests creation of review object
      self.assertFalse(Review.objects.filter(chef=self.test_chef_profile).exists())
      review_1 = Review.objects.create(patron=self.test_patron.patron,
                                       chef=self.test_chef_profile, stars=4)
      self.assertTrue(Review.objects.filter(chef=self.test_chef_profile).exists())

      # Tests link between review model and chef/patron model
      self.assertEqual(self.test_chef_profile, review_1.chef)
      self.assertEqual(self.test_patron.first_name, review_1.patron.user.first_name)

      # Tests average star rating update on chef model
      self.assertEqual(4, self.test_chef_profile.rating)
      review_2 = Review.objects.create(patron=self.test_patron.patron,
                                       chef=self.test_chef_profile, stars=2)
      self.assertEqual(2, len(Review.objects.filter(chef=self.test_chef_profile)))
      self.assertEqual(3, self.test_chef_profile.rating)
