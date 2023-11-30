from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import *
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from books.models import Book
from books.api.v1.serializers import *
from books.api.permissions import *


class BookModelViewSet(ModelViewSet):
    """a model view set for Book model"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "author"]
    ordering_fields = ["id", "price"]
