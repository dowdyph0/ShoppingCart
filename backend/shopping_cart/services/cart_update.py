
from django.db import transaction
from django.db.models.query import QuerySet
from shopping_cart.models import Cart, CartItems


@transaction.atomic()
def cart_update(cart: QuerySet[Cart], cart_item: int, quantity: float) -> QuerySet[Cart]:
    CartItems.objects.update_or_create(cart=cart, id=cart_item, defaults={'quantity': quantity}) 
    
    # if quantity is below zero we dont update the cart
    if quantity < 0:
        return cart

    # if quantity is zero the item is being removed of the cart
    if quantity == 0 or quantity == 0.0:
        CartItems.objects.filter(id=cart_item).delete()
    return cart
