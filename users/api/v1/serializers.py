from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from rest_framework import serializers


User = get_user_model()


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
        ]


class GroupSerializer(serializers.ModelSerializer):
    """a serializer for Group model when retreving object/objects"""

    class Meta:
        model = Group
        fields = ["id", "name", "permissions"]
