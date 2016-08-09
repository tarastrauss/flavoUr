from django.test import TestCase
from users.models import User
from chefs.models import Chef
from billing.models import Address
from django.core.exceptions import ValidationError

class AddressTestCase(TestCase):

    def setUp(self):

        self.test_user = User.objects.create(username="Anthony",
                                             first_name="Anthony")
        self.test_chef = User.objects.create(username="Foxy",
                                             first_name="Foxy")
        self.chef = Chef.objects.create(user=self.test_chef)

    def test_address_creation(self):
        '''
        Makes sure address is properly created and linked to a user or chef.
        '''

        # Tests creation of address and connection to user
        self.assertFalse(Address.objects.filter(user=self.test_user).exists())
        address = Address.objects.create(street_address='12', city='db', state='ca', zip='91789', user=self.test_user, title="yo" )
        self.assertTrue(Address.objects.filter(user=self.test_user).exists())
        self.assertEqual(self.test_user, address.user)

        # Tests creation of address and connection to chef
        self.assertFalse(Address.objects.filter(chef=self.chef).exists())
        address_2 = Address.objects.create(street_address='12', city='db', state='ca', zip='91789', chef=self.chef, title="yo" )
        self.assertTrue(Address.objects.filter(chef=self.chef).exists())
        self.assertEqual(self.chef, address_2.chef)

        # Tests validation error when chef and user is empty
        address_3 = Address(street_address='12', city='db', state='ca', zip='91789', title="yo")
        self.assertRaises(ValidationError, address_3.save)

