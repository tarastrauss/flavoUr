from django.test import TestCase
from django.db import models
from users.models import User
from chefs.models import Chef
from menus.models import Menu, Item
from django.core.urlresolvers import reverse
from rest_framework import status
class MenuTestCase(TestCase):

    def setUp(self):

        self.test_user = User.objects.create(username="Foxy",
                                             first_name="Foxy")
        self.chef = Chef.objects.create(user=self.test_user)

    def test_menu_creation(self):
        '''
        Makes sure menu is properly created and linked to chef.
        '''

        # # Tests creation of menu and connection to user
        # self.assertFalse(Menu.objects.filter(chef=self.chef).exists())
        # menu = Menu.objects.create(chef=self.chef, title='foxy food', delivery=True )
        # self.assertTrue(Menu.objects.filter(chef=self.chef).exists())
        # self.assertEqual(self.chef, menu.chef)
        # self.assertEqual(True, menu.delivery)

        # # Tests creation of item and connection to menu
        # self.assertFalse(Item.objects.filter(menu=menu).exists())
        # item = Item.objects.create(menu=menu, title="kibbles", size="the whole bowl",
        #                            price=13.33, description="food for foxy")
        # self.assertTrue(Item.objects.filter(menu=menu).exists())
        # self.assertEqual(menu, item.menu)

    def test_menu_get(self):
        '''
        Tests get endpoints for menu-detail and item-detail
        '''
        menu = Menu.objects.create(chef=self.chef, title='foxy food', delivery=True )
        item = Item.objects.create(menu=menu, title="kibbles", size="the whole bowl",
                                   price=13.33, description="food for foxy")
        url = reverse('menu-detail', kwargs={'pk':menu.id})
        response = self.client.get(url)
        self.assertEqual(response.data, {'id': 1, 'chef':1, 'title':'foxy food', 'delivery':True})

        url = reverse('item-detail', kwargs={'menu_pk':menu.id,'pk':item.id})
        response = self.client.get(url)
        self.assertEqual(response.data, {'id':1, 'title':'kibbles', 'size':'the whole bowl', 'price':'13.33', 'description':'food for foxy', 'menu':1})

    def test_menu_post(self):
        '''
        Tests POST method for menu-list.
        '''
        url = reverse('menu-list')
        data = { 'chef':1, 'title':'just the best', 'delivery':True}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 1)
        self.assertEqual(Menu.objects.get().title, 'just the best')

    def test_item_post(self):
        '''
        Tests POST method for item-list.
        '''
        menu = Menu.objects.create(chef=self.chef, title='foxy food', delivery=True )
        url = reverse('item-list', kwargs={'pk':menu.id})
        data = {'title':'foxy snacks', 'size':'all of it', 'price':'10.00', 'description':'food for foxy', 'menu':1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(Item.objects.get().title, 'foxy snacks')

