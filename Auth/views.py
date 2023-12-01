from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['id'] = user.id
        token['username'] = user.username
        token['permissions'] = [str(permission.codename) for permission in user.user_permissions.all()]
        token['email'] = user.email
        token['isSuperuser'] = user.is_superuser
        token['isStaff'] = user.is_staff

        return token


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def validate_access_token(request):
    try:
        AccessToken(request.accessToken)
        return Response({"detail": "Access token is valid."}, status=status.HTTP_200_OK)
    except TokenError:
        return Response({"detail": "Access token is not valid."}, status=status.HTTP_401_UNAUTHORIZED)

