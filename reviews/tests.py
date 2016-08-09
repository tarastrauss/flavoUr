from django.test import TestCase
from users.models import User
from chefs.models import Chef
from reviews.models import Review

class ReviewTestCase(TestCase):

    def setUp(self):

        self.user_1 = User.objects.create(username="HungryPerson",
                                               first_name="John")
        self.user_2 = User.objects.create(username="AwesomeChef",
                                             first_name="Jane")
        self.chef = Chef.objects.create(user=self.user_2)

    def test_chef_model(self):
      '''
      Tests creation of the Chef model and links to other models.
      '''

      # Tests creation of review object
      self.assertFalse(Review.objects.filter(chef=self.chef).exists())
      review_1 = Review.objects.create(user=self.user_1,
                                       chef=self.chef, stars=4)
      self.assertTrue(Review.objects.filter(chef=self.chef).exists())

      # Tests link between review model and chef/patron model
      self.assertEqual(self.chef, review_1.chef)
      self.assertEqual(self.user_1, review_1.user)

      # Tests average star rating update on chef model
      self.assertEqual(4, self.chef.rating)
      review_2 = Review.objects.create(user=self.user_1,
                                       chef=self.chef, stars=2)
      self.assertEqual(2, len(Review.objects.filter(chef=self.chef)))
      self.assertEqual(3, self.chef.rating)
