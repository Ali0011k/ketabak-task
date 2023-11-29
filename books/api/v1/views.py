from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import *
from books.models import Book
from books.api.v1.serializers import *
from books.api.v1.permissions import *


class BookModelViewSet(ModelViewSet):
    """a model view set for Book model"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]