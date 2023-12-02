from rest_framework import serializers
from books.api.v1.serializers import BookSerializer
from orders.models import BorrowedBooks
from users.api.v1.serializers import UserSerializer


class BorrowedBooksSerializer(serializers.ModelSerializer):
    """a serializer for BorrowedBooks model"""

    class Meta:
        model = BorrowedBooks
        fields = ["id", "user", "address", "books", "received_at", "validity_at"]


class BorrowedBooksGetActionSerializer(serializers.ModelSerializer):
    """a serializer for BorrowedBooks model"""

    user = UserSerializer(read_only=True)
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = BorrowedBooks
        fields = ["id", "user", "address", "books", "received_at", "validity_at"]
