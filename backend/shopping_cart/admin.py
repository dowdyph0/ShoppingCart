from django.contrib import admin

from shopping_cart.models import Cart, Item, CartItems


class ItemAdmin(admin.ModelAdmin):
    pass

class CartAdmin(admin.ModelAdmin):
    pass

class CartItemsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Item, ItemAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItems, CartItemsAdmin)
