from django.test import TestCase
from django.contrib.auth.models import User
from orders.models import BorrowedBooks


class TestBorrowedBooksModel(TestCase):
    """testing BorrowedBooks model"""

    def setUp(self):
        self.borrowedbook = BorrowedBooks.objects.first()

    def test_object_exist(self):
        self.assertTrue(self.borrowedbook)

    def test_object_equals(self):
        user = User.objects.first()
        self.assertEqual(self.borrowedbook.user, user)
