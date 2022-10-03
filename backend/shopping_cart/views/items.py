from rest_framework.generics import views
from rest_framework import serializers
from shopping_cart.models import Item


class ItemViewSet(views.ViewSet):
    class ItemListSerializer(serializers.ModelSerializer):
        class Meta:
            fields = "__all__"

    queryset = Item.Objects.all()
