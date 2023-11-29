from django.db import models
from django.contrib.auth.models import User
from books.models import Book


class BorrowedBooks(models.Model):
    """this is BorrowedBooks model"""

    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True)
    address = models.TextField()
    books = models.ManyToManyField(Book)
    received_at = models.DateTimeField(auto_now_add=True)
    validity_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        db_table = "BorrowedBooks"
        verbose_name = "Borrowed Book"
        verbose_name_plural = "Borrowed Books"
