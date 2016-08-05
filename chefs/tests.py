from django.test import TestCase
from users.models import User
from chefs.models import ChefInfo

class ChefTestCase(TestCase):

    def setUp(self):

        self.test_user = User.objects.create(username="Anthony")

    def test_chef_creation(self):
        '''
        Makes sure ChefInfo model is created and connected to user model.
        '''

        # Creates ChefInfo object
        chef_info = ChefInfo.objects.create(user_info=self.test_user)

        # Asserts chef object is created and linked to user
        self.assertEqual(1, len(ChefInfo.objects.all()))
        self.assertEqual(self.test_user.id, chef_info.user_info.id)
        self.assertEqual(chef_info.pk, self.test_user.chefinfo.pk)

