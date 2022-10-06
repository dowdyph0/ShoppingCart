import decimal
import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from shopping_cart.models import Cart, Item

from .utils import generate_dummy_png


class CartCheckOutTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_user", password="test", is_active=True)
        self.cart = self.user.cart
        self.item_1 = Item.objects.create(name="test1")
        self.item_2 = Item.objects.create(name="test2")
        self.item_1.image.save('image_1.png', generate_dummy_png())
        self.item_2.image.save('image_2.png', generate_dummy_png())
        self.quantity_1 = "2.00"
        self.quantity_2 = "4.00"
        self.country_code = 'US'
   
    def test_cart_checkout(self):
        json_data = {
            "cart_items": [
                {
                    "item_id": self.item_1.id,
                    "quantity": self.quantity_1
                },
                {
                    "item_id": self.item_2.id,
                    "quantity": self.quantity_2
                }
            ],
            "country_code": self.country_code
        }
        client = APIClient()
        client.login(username='test_user', password='test')
        jwt = RefreshToken.for_user(self.user)
        url = reverse("api:shopping_cart:checkout")
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {jwt.access_token}')
        response = client.post(url, data=json.dumps(json_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        cart_id = response.data.get("id")
        cart = Cart.objects.get(id=cart_id)
        self.assertEqual(cart.cart_items.all()[0].item.name, self.item_1.name)
        self.assertEqual(cart.cart_items.all()[1].item.name, self.item_2.name)
        self.assertEqual(cart.cart_items.all()[0].quantity, decimal.Decimal(self.quantity_1))
        self.assertEqual(cart.cart_items.all()[1].quantity, decimal.Decimal(self.quantity_2))
        self.assertEqual(cart.country.code, self.country_code)


