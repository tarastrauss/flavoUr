from django.test import TestCase
from users.models import User
from chefs.models import Chef

class ChefTestCase(TestCase):

    def setUp(self):

        self.test_user = User.objects.create(username="Anthony",
                                             first_name="Anthony")

    def test_chef_creation(self):
        '''
        Makes sure ChefInfo model is created and connected to user model.
        '''

        # Creates ChefInfo object
        chef_info = Chef.objects.create(user=self.test_user)

        # Asserts chef object is created and linked to user
        self.assertEqual(1, len(Chef.objects.all()))
        self.assertEqual(self.test_user, chef_info.user)
        self.assertEqual(chef_info, self.test_user.chef)

