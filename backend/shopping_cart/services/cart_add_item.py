from django.db import transaction
from shopping_cart.models import CartItems
from shopping_cart.models import Cart
from django.db.models import QuerySet

@transaction.atomic()
def cart_add_item(cart: QuerySet[Cart], item: int) -> QuerySet[Cart]:
    queryset = CartItems.objects.filter(cart=cart, item_id=item)
    count = queryset.count()
    
    # if the cart already contains the item
    if count > 0:
        cart_item = queryset.last()
        quantity = cart_item.quantity + 1
        queryset.update(quantity=quantity)
    
    # if the item does not exist in the cart
    if count == 0:
        item = CartItems.objects.create(cart=cart, item_id=item, quantity=1.0)
    return cart