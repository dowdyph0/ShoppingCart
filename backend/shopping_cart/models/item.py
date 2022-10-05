from django.db import models
from djmoney.models.fields import MoneyField

from .base_model import BaseModel


class Item(BaseModel):
    name = models.CharField(max_length=250)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    image = models.ImageField(upload_to='item_images')
    
    def __str__(self):
        return self.name
