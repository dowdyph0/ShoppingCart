from .base_model import BaseModel
from django.db import models
from djmoney.models.fields import MoneyField


class Cart(BaseModel):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    item = models.ManyToManyField('shopping_cart.Item', through='shopping_cart.ItemQty')
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    def __str__(self):
        return f'{self.user.get_full_name} ({self.price} {self.price_currency})'