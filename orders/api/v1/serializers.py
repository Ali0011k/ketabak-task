from rest_framework import serializers
from books.api.v1.serializers import BookSerializer
from orders.models import BorrowedBooks


class BorrowedBooksSerializer(serializers.ModelSerializer):
    """a serializer for BorrowedBooks model"""

    class Meta:
        model = BorrowedBooks
        fields = ["id", "user", "address", "books", "received_at", "validity_at"]
