from django.db import models

from .base_model import BaseModel


class ItemQty(BaseModel):
    item = models.ForeignKey('shopping_cart.Item', on_delete=models.CASCADE)
    cart = models.ForeignKey('shopping_cart.Cart', on_delete=models.CASCADE)
    qty = models.FloatField(default=0)

    def __str__(self):
        return f'{self.cart} - {self.item} #{self.qty}'
