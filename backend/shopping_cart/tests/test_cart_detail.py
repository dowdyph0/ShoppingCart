from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from shopping_cart.models import CartItems, Item

from .utils import generate_dummy_png


class CartDetailTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_user", password="test")
        self.cart = self.user.cart
        self.item_1 = Item.objects.create(name="test1")
        self.item_2 = Item.objects.create(name="test2")
        self.item_1.image.save('image_1.png', generate_dummy_png())
        self.item_2.image.save('image_2.png', generate_dummy_png())
        self.cart_item_1 = CartItems.objects.create(cart=self.cart, item=self.item_1, quantity=1)
        self.cart_item_2 = CartItems.objects.create(cart=self.cart, item=self.item_2, quantity=2)
        self.cart.cart_items.add(self.cart_item_1)
        self.cart.cart_items.add(self.cart_item_2)

    def test_cart_created_on_user_create(self):
        cart = getattr(self.user, "cart")
        self.assertIsNotNone(cart)

    def test_cart_detail_correct(self):
        client = APIClient()
        jwt = RefreshToken.for_user(self.user)
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {jwt.access_token}')
        url = reverse("api:shopping_cart:details", kwargs={'id': self.cart.id})
        response = client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["user"]["username"], self.user.username)
        self.assertEqual(response.data["cart_items"][0]["item"]["name"], self.item_1.name)
        self.assertEqual(response.data["cart_items"][1]["item"]["name"], self.item_2.name)
