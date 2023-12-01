from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import *
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
from users.api.v1.serializers import *



User = get_user_model()

class UserModelViewSet(ModelViewSet):
    """a model view set for User model"""
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ["id", "is_superuser", "is_staff", "is_active", "is_verified"]
    search_fields = ["username", "email"]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return UserGetActionSerializer
        else:
            return self.serializer_class


class PermissionModelViewSet(ModelViewSet):
    """a model view set for Permission model"""
    
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ["id"]
    search_fields = ["name"]


class GroupModelViewSet(ModelViewSet):
    """a model view set for Group model"""
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ["id"]
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return GroupGetActionSerializer
        else:
            return self.serializer_class
