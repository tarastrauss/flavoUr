from django.test import TestCase
from django.db import models
from users.models import User
from chefs.models import Chef
from menus.models import Menu, Item
from django.core.urlresolvers import reverse
import json
from rest_framework.test import APIClient
from flavoUr.urls import urlpatterns
from django.test import TransactionTestCase

class MenuTestCase(TransactionTestCase):

    def setUp(self):

        # self.api_client = APIClient()
        self.test_user = User.objects.create(username="Foxy", first_name="Foxy",
                                             password='bone')
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

    def test_menu_get_and_post(self):

        url = reverse('menu_post')
        items = [{'title': 'Soup', 'size': 'Serves 5', 'description': 'Better then '
            'your mom\'s!'},
           {'title': 'Noodles', 'size': 'Serves 5', 'description': 'These noodles '
            'make the soup even better!'}]
        params = {'title': 'Matza Ball Soup!', 'delivery': True, 'items': items}
        self.client.login(username=self.test_user.username, password=self.test_user.password)
        response = self.client.post(url, params)
        # data = json.loads(response).get('data', {})
        # expected = {u'chef': u'foxy'}
        print 'the response is %s' % response.content
         # data = json.loads(response).get('data', {})









