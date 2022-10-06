from ast import Bytes
from rest_framework import serializers
from rest_framework.views import APIView
from shopping_cart.models import Item
from shopping_cart.selectors import items_list
from rest_framework.response import Response


class ItemListApi(APIView):
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
        out_serializer = self.OutputSerializer(items, many=True, context={'request': request})
        return Response(out_serializer.data)