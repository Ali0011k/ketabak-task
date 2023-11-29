from django.test import TestCase
from books.models import Book


class TestBookModel(TestCase):
    """testing book model"""

    def setUp(self):
        self.book = Book.objects.get(id=1)

    def test_book_exist(self):
        """testing book is exist"""
        self.assertTrue(self.book)

    def test_book_equals(self):
        """testing book model is equals with created book"""
        book = Book.objects.first()
        self.assertEqual(book, self.book)
