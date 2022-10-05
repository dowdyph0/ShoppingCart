from shopping_cart.models import Item
from django.db.models.query import QuerySet


def items_list() -> QuerySet[Item]:
    qs = Item.objects.all()
    return qs
