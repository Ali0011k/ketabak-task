from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from decouple import config

User = get_user_model()


class TestUserApi(TestCase):
    """testing user apis"""

    def setUp(self):
        """setting up test settings"""

        self.user = User.objects.first()
        self.api_client = APIClient()

    def test_get_user(self):
        """testing get a user in api"""

        self.api_client.force_authenticate(self.user)
        url = reverse("users:api-v1:users-list")
        response = self.api_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        """creating a user with valid data"""

        self.api_client.force_authenticate(self.user)
        data = {
            "username": "username_for_test_users_app",
            "email": "testemail_for_test_users_app@test.com",
            "password": config("DJANGO_SUPERUSER_PASSWORD", cast=str),
            "is_superuser": True,
            "is_active": True,
            "is_staff": True,
            "is_verified": True,
        }

        url = reverse("users:api-v1:users-list")
        respons = self.api_client.post(url, data)

        self.assertEqual(respons.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(id=2).username, "username_for_test_users_app")

    def test_create_user_with_invalid_data(self):
        """creating a user with invalid data"""

        self.api_client.force_authenticate(self.user)
        data = {
            "username": "username_for_test_users_app",
            "is_superuser": True,
        }

        url = reverse("users:api-v1:users-list")
        respons = self.api_client.post(url, data)

        self.assertEqual(respons.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_without_permission(self):
        """creating a user without permission"""

        data = {
            "username": "username_for_test_users_app",
            "email": "testemail_for_test_users_app@test.com",
            "password": config("DJANGO_SUPERUSER_PASSWORD", cast=str),
            "is_superuser": True,
            "is_active": True,
            "is_staff": True,
            "is_verified": True,
        }

        url = reverse("users:api-v1:users-list")
        respons = self.api_client.post(url, data)

        self.assertEqual(respons.status_code, status.HTTP_401_UNAUTHORIZED)
