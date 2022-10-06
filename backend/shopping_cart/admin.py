from django.contrib import admin

from shopping_cart.models import Cart, Item, CartItems


class ItemAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'price',
        'image',
    ]

    list_editable = [
        'name',
        'price',
        'image',
    ]

class CartAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'country',
        'price',
    ]

    list_editable = [
        'user',
        'country',
    ]

class CartItemsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'item',
        'quantity',
        'cart',
        'price',
    ]

    list_editable = [
        'item',
        'quantity',
        'cart',
    ]

admin.site.register(Item, ItemAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItems, CartItemsAdmin)
