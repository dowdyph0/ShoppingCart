from .base_model import BaseModel
from django.db import models
from djmoney.models.fields import Money
from django.db.models import F
from django.db.models import Sum
from djmoney.models.fields import MoneyField
from django.db import transaction


class Cart(BaseModel):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    items = models.ManyToManyField('shopping_cart.ItemQty')
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    
    def __str__(self):
        return f'{self.user.username} - {self.price}'

    @transaction.atomic()
    def update_price(self):
        total_price = 0
        for item in self.items.all():
            new_price = item.update_price()
            total_price += new_price.amount
        self.price = Money(total_price, 'USD')
        self.save()
        return self.price