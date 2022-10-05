from api.pagination import LimitOffsetPagination, get_paginated_response
from djmoney.models.fields import MoneyField
from rest_framework import serializers
from rest_framework.views import APIView
from shopping_cart.models import Item
from shopping_cart.selectors import items_list


class ItemListApi(APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 1

    class OutputSerializer(serializers.ModelSerializer):
        image_url = serializers.SerializerMethodField()

        def get_image_url(self, obj):
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url)

        class Meta:
            model = Item
            fields = (
                'id',
                'name',
                'price',
                'price_currency',
                'image_url',
            )

    def get(self, request):
        items = items_list()

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=items,
            request=request,
            view=self
        )
