from django.urls import path, include

urlpatterns = [
    path('auth/', include(('jwt_auth.urls', 'jwt_auth'))),
    path('shop/', include(('shopping_cart.urls', 'shopping_cart'))),
]