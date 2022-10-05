from typing import OrderedDict
from api.utils import inline_serializer
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from shopping_cart.models import Cart, Item
from shopping_cart.selectors import cart_detail
from shopping_cart.services import cart_update


def get_image_url(instance, obj):
    request = instance.context.get('request')
    return request.build_absolute_uri(obj.image.url)


class CartDetailApi(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        user = inline_serializer(many=False, fields={
            'id': serializers.IntegerField(),
            'username': serializers.CharField(),
            'first_name': serializers.CharField(),
            'last_name': serializers.CharField()
        })
        
        price = serializers.DecimalField(source='price.amount', max_digits=14, decimal_places=2)
        price_currency = serializers.CharField(source='price.currency')

        class Meta:
            model = Cart
            depth = 4
            fields = (
                'id',
                'user',
                'items',
                'price',
                'price_currency',
            )

    def get(self, request):
        cart = cart_detail(request.user)
        serializer = self.OutputSerializer(cart, many=False, context={'request': request})
        return Response(serializer.data)


class CartUpdateApi(APIView):
    class InputSerializer(serializers.Serializer):
        item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
        qty = serializers.DecimalField(max_digits=14, decimal_places=2)

    class OutputSerializer(serializers.ModelSerializer):
        user = inline_serializer(many=False, fields={
            'id': serializers.IntegerField(),
            'username': serializers.CharField(),
            'first_name': serializers.CharField(),
            'last_name': serializers.CharField()
        })
        
        price = serializers.DecimalField(source='price.amount', max_digits=14, decimal_places=2)
        price_currency = serializers.CharField(source='price.currency')

        class Meta:
            model = Cart
            depth = 4
            fields = (
                'id',
                'user',
                'items',
                'price',
                'price_currency',
            )


    def post(self, request):
        in_serializer = self.InputSerializer(data=request.data, many=False, context={'request': request})
        if in_serializer.is_valid():
            cart = cart_update(request.user, in_serializer.data)
            out_serializer = self.OutputSerializer(cart, many=False, context={'request': request})
            return Response(out_serializer.data)