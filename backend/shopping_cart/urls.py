from django.urls import path


from .apis import CartDetailApi, ItemListApi, CartUpdateApi

urlpatterns = [
    path('items/', ItemListApi.as_view(), name='items'),
    path('cart/', CartDetailApi.as_view(),  name='shopping_cart'),
    path('cart/update/', CartUpdateApi.as_view(), name='shopping_cart_update'),
]
