from typing import OrderedDict
from xml.dom import ValidationErr
from api.utils import inline_serializer
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from shopping_cart.models.cart_items import CartItems
from shopping_cart.models import Cart, Item
from shopping_cart.services import cart_update
from shopping_cart.services import cart_add_item
from shopping_cart.services import cart_checkout
from django.shortcuts import get_object_or_404
from rest_framework import status

def get_image_url(instance, obj):
    request = instance.context.get('request')
    return request.build_absolute_uri(obj.image.url)


class OutputSerializer(serializers.ModelSerializer):
    user = inline_serializer(many=False, fields={
        'id': serializers.IntegerField(),
        'username': serializers.CharField(),
        'first_name': serializers.CharField(),
        'last_name': serializers.CharField()
    })
    
    price = serializers.DecimalField(source='price.amount', max_digits=14, decimal_places=2)
    price_currency = serializers.CharField(source='price.currency')
    country_code = serializers.CharField(source='country.code')
    country_name = serializers.CharField(source='country.name')
    cart_items = inline_serializer(many=True, fields={
        'id': serializers.IntegerField(),
        'quantity': serializers.DecimalField(max_digits=14, decimal_places=2),
        'price': serializers.DecimalField(source='price.amount', max_digits=14, decimal_places=2),
        'price_currency': serializers.CharField(source='price.currency'),
        'item': inline_serializer(many=False, fields={
            'id': serializers.IntegerField(),
            'name': serializers.CharField(),
            'price': serializers.DecimalField(source='price.amount', max_digits=14, decimal_places=2),
            'price_currency': serializers.CharField(source='price.currency'),
            'image_url': serializers.SerializerMethodField(),
            'get_image_url': get_image_url,
        })
    })


    class Meta:
            model = Cart
            depth = 2
            fields = (
                'id',
                'user',
                'cart_items',
                'price',
                'price_currency',
                'country_code',
                'country_name',
            )


class CartDetailApi(APIView):    
    def get(self, request, id=None):
        cart = get_object_or_404(Cart, pk=id)
        serializer = OutputSerializer(cart, many=False, context={'request': request})
        return Response(serializer.data)


class CartUpdateApi(APIView):
    class InputSerializer(serializers.Serializer):
        cart_item = serializers.PrimaryKeyRelatedField(queryset=CartItems.objects.all())
        qty = serializers.DecimalField(max_digits=14, decimal_places=2)

    def post(self, request, id=None):
        cart = get_object_or_404(Cart, pk=id)
        in_serializer = self.InputSerializer(data=request.data, many=False, context={'request': request})
        if in_serializer.is_valid():
            cart_item = in_serializer.data.get('cart_item')
            quantity = float(in_serializer.data.get('qty'))
            cart = cart_update(cart, cart_item, quantity)
            out_serializer = OutputSerializer(cart, many=False, context={'request': request})
            return Response(out_serializer.data)
        else:
            return Response(in_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartAddItemApi(APIView):
    class InputSerializer(serializers.Serializer):
        item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    
    def post(self, request, id=None):
        cart = get_object_or_404(Cart, pk=id)
        in_serializer = self.InputSerializer(data=request.data, many=False, context={'request': request})
        if in_serializer.is_valid():
            cart = cart_add_item(cart, in_serializer.data.get("item"))
            out_serializer = OutputSerializer(cart, many=False, context={'request': request})
            return Response(out_serializer.data)
        else:
            return Response(in_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def validate_quantity(instance, value):
    if value < 0:
        raise ValidationErr("Item quantity must be positive decimal")
    return value


class CartCheckoutApi(APIView):
    class InputSerializer(serializers.Serializer):
        country_code = serializers.CharField()
        cart_items = inline_serializer(many=True, fields={
            "item_id": serializers.PrimaryKeyRelatedField(queryset=Item.objects.all()),
            "quantity": serializers.DecimalField(max_digits=14, decimal_places=2),
            "validate_quantity": validate_quantity,
        })

    class OutputSerializer(serializers.ModelSerializer):
        id = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all)
        class Meta:
            model = Cart
            fields = ["id"]

    def post(self, request):
        in_serializer = self.InputSerializer(data=request.data)
        if in_serializer.is_valid():
            country_code = in_serializer.data.get("country_code")
            cart_items = in_serializer.data.get("cart_items")
            cart = cart_checkout(request.user, country_code, cart_items)
            return Response(self.OutputSerializer(cart, many=False).data)
        else:
            return Response(in_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
