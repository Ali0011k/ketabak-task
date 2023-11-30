from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    """book model serializer"""

    class Meta:
        model = Book
        fields = [
            "id",
            "name",
            "author",
            "price",
            "description",
            "cover_image",
        ]
