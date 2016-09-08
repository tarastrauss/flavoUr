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
        self.menu = Menu.objects.create(chef=self.chef, title='foxy food', delivery=True )
        self.item = Item.objects.create(menu=self.menu, title="kibbles", size="the whole bowl",
                                   price=13.33, description="food for foxy")

    def test_menu_creation(self):
        '''
        Makes sure menu is properly created and linked to chef.
        '''

        # Tests creation of menu and connection to user
        self.assertFalse(Menu.objects.filter(title='foxys favorites').exists())
        menu = Menu.objects.create(chef=self.chef, title='foxys favorites', delivery=True )
        self.assertTrue(Menu.objects.filter(title='foxys favorites').exists())
        self.assertEqual(self.chef, menu.chef)
        self.assertEqual(True, menu.delivery)

        # Tests creation of item and connection to menu
        self.assertFalse(Item.objects.filter(menu=menu).exists())
        item = Item.objects.create(menu=menu, title="kibbles", size="the whole bowl",
                                   price=13.33, description="food for foxy")
        self.assertTrue(Item.objects.filter(menu=menu).exists())
        self.assertEqual(menu, item.menu)

    def test_menu_get(self):
        '''
        Tests GET method for menu-detail and item-detail
        '''

        url = reverse('menu-detail', kwargs={'pk':self.menu.id})
        response = self.client.get(url)
        self.assertEqual({'id': 1, 'chef':1, 'title':'foxy food', 'delivery':True}, response.data)

        url = reverse('item-detail', kwargs={'menu_pk':self.menu.id,'pk':self.item.id})
        response = self.client.get(url)
        self.assertEqual({'id':1, 'title':'kibbles', 'size':'the whole bowl', 'price':'13.33', 'description':'food for foxy', 'menu':1}, response.data)

    def test_menu_post(self):
        '''
        Tests POST method for menu-list.
        '''
        url = reverse('menu-list')
        data = { 'chef':self.chef.pk, 'title':'just the best', 'delivery':True}
        response = self.client.post(url, data, format='json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertTrue(Menu.objects.filter(title='just the best').exists())

    def test_item_post(self):
        '''
        Tests POST method for item-list.
        '''
        url = reverse('item-list', kwargs={'pk':self.menu.id})
        data = {'title':'foxy snacks', 'size':'all of it', 'price':10.00, 'description':'food for foxy', 'menu':self.menu.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertTrue(Item.objects.filter(title= 'foxy snacks').exists())

    def test_get_menu_root(self):
        '''
        Tests GET method for menu-root
        '''
        url = reverse('menu-root', kwargs={'pk':self.menu.id})
        response = self.client.get(url, format='json')
        self.assertEqual({
            "Menu": {
                "id": 1,
                "chef": 1,
                "title": "foxy food",
                "delivery": True
            },
            "Items": [{"id":1,"title":"kibbles","description":"food for foxy", "price":'13.33', "size":"the whole bowl", "menu":1}]
        }, response.data)

