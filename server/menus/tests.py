from django.test import TestCase
from django.db import models
from users.models import User
from chefs.models import Chef
from menus.models import Menu, Item

class MenuTestCase(TestCase):

    def setUp(self):

        self.test_user = User.objects.create(username="Foxy",
                                             first_name="Foxy")
        self.chef = Chef.objects.create(user=self.test_user)

    def test_menu_creation(self):
        '''
        Makes sure menu is properly created and linked to chef.
        '''

        # Tests creation of menu and connection to user
        self.assertFalse(Menu.objects.filter(chef=self.chef).exists())
        menu = Menu.objects.create(chef=self.chef, title='foxy food', delivery=True )
        self.assertTrue(Menu.objects.filter(chef=self.chef).exists())
        self.assertEqual(self.chef, menu.chef)
        self.assertEqual(True, menu.delivery)

        # Tests creation of item and connection to menu
        self.assertFalse(Item.objects.filter(menu=menu).exists())
        item = Item.objects.create(menu=menu, title="kibbles", size="the whole bowl",
                                   price=13.33, description="food for foxy")
        self.assertTrue(Item.objects.filter(menu=menu).exists())
        self.assertEqual(menu, item.menu)
