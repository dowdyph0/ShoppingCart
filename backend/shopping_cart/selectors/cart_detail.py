from shopping_cart.models import Cart
from django.db.models.query import QuerySet
from django.contrib.auth.models import User


def cart_detail(user: QuerySet[User]) -> QuerySet[Cart]:
    cart = Cart.objects.filter(user_id=user.id).order_by('-updated_at').first()
    return cart
