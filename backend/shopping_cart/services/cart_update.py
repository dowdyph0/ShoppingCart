from django.contrib.auth.models import User
from django.db import transaction
from django.db.models.query import QuerySet
from rest_framework.serializers import Serializer
from shopping_cart.models import Cart, ItemQty
from shopping_cart.selectors import cart_detail


@transaction.atomic()
def cart_update(user: QuerySet[User], serializer: Serializer) -> QuerySet[Cart]:
    cart = cart_detail(user)
    item = serializer['item']
    qty = serializer['qty']
    quantity = float(qty)
    queryset = cart.items.filter(item_id=item)
    count = queryset.count()
    print(cart, item, quantity, count)
    if count > 0 and quantity > 0:
        cart.items.filter(item_id=item).update(qty=qty)
    if count == 0 and quantity > 0:
        item_qty = ItemQty(item_id=item, qty=qty)
        item_qty.save()
        cart.items.add(item_qty.id)
    if quantity == 0 or quantity == 0.0:
        queryset.delete()
    cart.update_price()
    return cart
