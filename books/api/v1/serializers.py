from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    """book model serializer"""

    short_content = serializers.URLField(source="short_description", read_only=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "name",
            "author",
            "price",
            "description",
            "cover_image",
            "short_content",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")
        if request and request != None:
            if request.parser_context:
                if request.parser_context.get("kwargs"):
                    data.pop("short_content")
                else:
                    data.pop("description")
        return data
