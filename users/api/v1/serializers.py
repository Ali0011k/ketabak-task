from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from rest_framework import serializers


User = get_user_model()



class PermissionSerializer(serializers.ModelSerializer):
    """a serializer for serializing user permissions"""

    class Meta:
        model = Permission
        fields = [
            "id",
            "name",
            "content_type",
            "codename"
        ]

class UserSerializer(serializers.ModelSerializer):
    """a serializer for User model"""
    
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_superuser",
            "is_staff",
            "is_active",
            "is_verified",
            "date_joined",
            "user_permissions"
        ]

class UserGetActionSerializer(serializers.ModelSerializer):
    """a serializer for User model when retreving object/objects"""
    
    user_permissions = PermissionSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_superuser",
            "is_staff",
            "is_active",
            "is_verified",
            "date_joined",
            "user_permissions"
        ]


class GroupSerializer(serializers.ModelSerializer):
    """a serializer for Group model when retreving object/objects"""

    class Meta:
        model = Group
        fields = [
            "id",
            "name",
            "permissions"
        ]


class GroupGetActionSerializer(serializers.ModelSerializer):
    """a serializer for Group model"""

    permissions = PermissionSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = [
            "id",
            "name",
            "permissions"
        ]
