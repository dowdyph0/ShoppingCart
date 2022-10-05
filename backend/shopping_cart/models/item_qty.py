from django.db import models

from .base_model import BaseModel
from djmoney.models.fields import Money, MoneyField


class ItemQty(BaseModel):
    item = models.ForeignKey('shopping_cart.Item', on_delete=models.CASCADE)
    qty = models.DecimalField(default=0, max_digits=14, decimal_places=2)
    price = MoneyField(max_digits=14, decimal_places=2)

    def __str__(self):
        return f'{self.item} #{self.qty} {self.price}'

    def update_price(self):
        self.price = Money(self.item.price.amount * self.qty, self.item.price.currency)
        self.save()
        return self.price