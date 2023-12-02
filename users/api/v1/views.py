from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import *
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.api.v1.serializers import *
import jwt

User = get_user_model()


class UserModelViewSet(ModelViewSet):
    """a model view set for User model"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ["id", "is_superuser", "is_staff", "is_active", "is_verified"]
    search_fields = ["username", "email"]


class VerifyUserApiView(APIView):
    """verifying user using email"""

    queryset = User.objects.all()

    def get(self, request, token, *args, **kwargs):
        try:
            decoded_token = jwt.decode(
                token,
                settings.SIMPLE_JWT["SIGNING_KEY"],
                settings.SIMPLE_JWT["ALGORITHM"],
            )
        except:
            return Response(
                {"your token is invalid or expired"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.get(id=decoded_token.get("user_id"))
        if user.is_verified == True:
            return Response(
                {"you account is already verified"}, status=status.HTTP_403_FORBIDDEN
            )
        else:
            user.is_verified = True
            user.save()
            return Response({"detail": "your account is verified"})
