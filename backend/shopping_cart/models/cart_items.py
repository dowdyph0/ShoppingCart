from django.db import models

from .base_model import BaseModel
from djmoney.models.fields import Money, MoneyField


class CartItems(BaseModel):
    item = models.ForeignKey('shopping_cart.Item', on_delete=models.CASCADE)
    quantity = models.DecimalField(default=0, max_digits=14, decimal_places=2)
    cart = models.ForeignKey('shopping_cart.Cart', on_delete=models.CASCADE, related_name="cart_items")

    def __str__(self):
        return f'{self.item} #{self.quantity} {self.price}'

    @property
    def price(self):
        return self.quantity * self.item.price

    class Meta:
        unique_together = ('item', 'cart')