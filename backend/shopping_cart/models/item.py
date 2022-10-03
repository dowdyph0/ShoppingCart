from django.db import models
from djmoney.models.fields import MoneyField

from .base_model import BaseModel


class Item(BaseModel):
    name = models.CharField(max_length=250)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    
    def __str__(self):
        return f'{self.name} # {self.price} {self.price_currency}'
