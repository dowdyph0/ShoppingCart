from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import QuerySet
from shopping_cart.models import Cart, CartItems


@transaction.atomic()
def cart_checkout(user: QuerySet[User], country_code: str, cart_items: list[dict]):
    # create or obtain the users's cart
    cart, created = Cart.objects.get_or_create(user=user, defaults={"country": country_code,})
    
    # clear existing items
    CartItems.objects.filter(cart=cart).delete()

    # foreach item add it to cart if quantity > 0
    for item in cart_items:
        quantity = float(item.get("quantity", "0.0"))
        if quantity > 0:
            CartItems.objects.create(cart=cart, item_id=item.get("item_id"), quantity=item.get("quantity"))

    return cart
