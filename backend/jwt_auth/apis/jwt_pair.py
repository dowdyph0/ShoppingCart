from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class OutputSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['cart_id'] = user.cart.id
        token['is_superuser'] = user.is_superuser
        return token

class TokenObtainPairApi(TokenObtainPairView):
    serializer_class = OutputSerializer