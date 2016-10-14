from django.test import TestCase
from orders.models import Order
from users.models import User
from chefs.models import Chef
from menus.models import Menu, Item
from billing.models import Address
from django.db.models import Sum

class OrderTestCase(TestCase):

    def setUp(self):
        '''
        '''
        self.user_1 = User.objects.create(username="Teddy",
                                               first_name="Teddy")
        self.user_2 = User.objects.create(username="Foxy",
                                             first_name="Foxy")
        self.chef = Chef.objects.create(user=self.user_2)

        self.billing_address = Address.objects.create(street_address='1234', city='db', state='ca', zip='91789',
                                                                user=self.user_1, title="yo" )
        self.menu = Menu.objects.create(chef=self.chef, title='foxy food', delivery=True )

        self.item_1 = Item.objects.create(menu=self.menu, title="kibbles", size="the whole bowl",
                                   price=20.00, description="food for foxy")
        self.item_2 = Item.objects.create(menu=self.menu, title="tastybits", size="the whole bowl",
                                   price=15.00, description="food for tee")
        self.item_3 = Item.objects.create(menu=self.menu, title="tastysnacks", size="a quad",
                                   price=420.00, description="food")
    def test_order_model(self):
        '''
        Makes sure an order is linked between a user and chef.
        '''
        # Tests the creation of an order linked between a chef and a customer
        self.assertFalse(Order.objects.filter(customer=self.user_1).exists())
        order = Order.objects.create(customer=self.user_1, chef=self.chef,
                                     customer_address=self.billing_address)
        self.assertTrue(Order.objects.filter(customer=self.user_1).exists())

        # Adds items to the menu, makes sure that items are properly linked to the menu.
        self.assertEqual(0, order.item.count())
        order.item.add(1)
        order.item.add(2)
        self.assertEqual(2, order.item.count())

        # Makes sure items in order match the ones created.
        first_item = order.item.get(title='kibbles')
        self.assertEqual(self.item_1, first_item)
        second_item = order.item.get(title='tastybits')
        self.assertEqual(self.item_2, second_item)

        # Tests the total_price field, value should reflect the subtotal of the items ordered.
        self.assertEqual(35.00, order.total_price)

        # Adds third order, makes sure its correctly populated in the order instance and checks to see the price changes.
        order.item.add(3)
        third_item = order.item.get(title='tastysnacks')
        self.assertEqual(3, order.item.count())
        self.assertEqual(self.item_3,third_item)
        self.assertEqual(455.00, order.total_price)
