from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .apis import TokenObtainPairApi

urlpatterns = [
    path('token/', TokenObtainPairApi.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
