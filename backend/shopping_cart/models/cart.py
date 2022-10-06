from django.contrib.auth.models import User
from django.db import models, transaction
from django.db.models import F, Sum
from django.db.models.signals import post_save
from django_countries.fields import CountryField
from djmoney.models.fields import Money, MoneyField

from .base_model import BaseModel


class Cart(BaseModel):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name="cart")
    country = CountryField(default='us')

    def __str__(self):
        return f'({self.country}) {self.user.username} - {self.price}'

    @property
    def price(self):
        total = Money(0.0, 'USD')
        for cart_item in self.cart_items.all():
            total += cart_item.price
        return total

def create_user_cart(sender, instance, created, **kwargs):  
    if created:  
       cart, created = Cart.objects.get_or_create(user=instance)  

post_save.connect(create_user_cart, sender=User) 
