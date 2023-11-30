from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from books.models import Book
from orders.models import BorrowedBooks


class TestBorrowedBooksApi(APITestCase):
    """test borrowedbooks model's api"""

    def setUp(self):
        """setting up api client"""
        self.api_client = APIClient()

    def test_get_borrowedbooks(self):
        """testing borrowedbooks are equal with database objects"""
        user = User.objects.first()
        self.api_client.force_authenticate(user)
        response = self.api_client.get(reverse("orders:api-v1:borrowedbooks-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_borrowedbook_create(self):
        """creating a borrowedbooks with a valid data"""

        user = User.objects.first()
        self.api_client.force_authenticate(user)

        data = {
            "user": user.pk,
            "address": "test address for api",
            "books": [],
        }

        for book in Book.objects.all():
            data["books"].append(book.pk)

        url = reverse("orders:api-v1:borrowedbooks-list")
        response = self.api_client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BorrowedBooks.objects.count(), 2)
        self.assertEqual(BorrowedBooks.objects.get(id=2).user, user)

    def test_borrowedbooks_create_with_invalid_data(self):
        """creating a borrowedbooks with invalid data"""
        user = User.objects.first()
        self.api_client.force_authenticate(user)

        data = {
            "user": user.pk,
            "books": "",
        }

        url = reverse("orders:api-v1:borrowedbooks-list")
        response = self.api_client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_book_unauthorized(self):
        """creating a book with out user logged in"""
        user = User.objects.first()

        data = {
            "user": user.pk,
            "address": "test address for api",
            "books": [],
        }

        for book in Book.objects.all():
            data["books"].append(book.pk)

        url = reverse("orders:api-v1:borrowedbooks-list")
        response = self.api_client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
