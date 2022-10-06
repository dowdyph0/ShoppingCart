from django.urls import path

from .apis import CartDetailApi, ItemListApi, CartUpdateApi, CartAddItemApi, CartCheckoutApi

urlpatterns = [
    path('items/', ItemListApi.as_view(), name='items'),
    path('cart/<int:id>/', CartDetailApi.as_view(),  name='details'),
    path('cart/<int:id>/update/', CartUpdateApi.as_view(), name='update'),
    path('cart/<int:id>/add/', CartAddItemApi.as_view(), name='add_item'),
    path('cart/checkout/', CartCheckoutApi.as_view(), name="checkout"),
]
