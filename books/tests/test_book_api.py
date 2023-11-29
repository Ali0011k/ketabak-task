from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from books.models import Book
import requests


class TestBookApi(APITestCase):
    """test book model's api"""

    def setUp(self):
        """setting up api client"""
        self.api_client = APIClient()

    def test_get_books(self):
        """testing books are equal with database objects"""
        response = self.api_client.get(reverse("books:api-v1:books-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_create(self):
        """creating a book with a valid data"""
        user = User.objects.first()
        self.api_client.force_authenticate(user=user)
        img_url = "https://img.freepik.com/free-photo/digital-painting-mountain-with-colorful-tree-foreground_1340-25699.jpg"
        image_request = requests.get(url=img_url)
        data = {
            "name": "Test Book For Api",
            "author": "Test Books Author",
            "price": 10000,
            "description": "This is a book for testing book Api",
        }
        image_file = SimpleUploadedFile(
            "test_image.jpg", image_request.content, content_type="image/jpeg"
        )
        data["cover_image"] = image_file

        url = reverse("books:api-v1:books-list")
        response = self.api_client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=2).name, "Test Book For Api")

    def test_book_create_with_invalid_data(self):
        """creating a book with invalid data"""
        user = User.objects.first()
        self.api_client.force_authenticate(user=user)
        data = {
            "author": "Test Books Author",
            "price": 10000,
            "description": "This is a book for testing book Api",
        }
        url = reverse("books:api-v1:books-list")
        response = self.api_client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_book_unauthorized(self):
        """creating a book with out user logged in"""
        img_url = "https://img.freepik.com/free-photo/digital-painting-mountain-with-colorful-tree-foreground_1340-25699.jpg"
        image_request = requests.get(url=img_url)
        data = {
            "name": "Test Book For Api",
            "author": "Test Books Author",
            "price": 10000,
            "description": "This is a book for testing book Api",
        }
        image_file = SimpleUploadedFile(
            "test_image.jpg", image_request.content, content_type="image/jpeg"
        )
        data["cover_image"] = image_file

        url = reverse("books:api-v1:books-list")
        response = self.api_client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
