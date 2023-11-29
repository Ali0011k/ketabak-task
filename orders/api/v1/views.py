from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import *
from books.api.v1.permissions import IsAdminOrReadOnly
from orders.api.v1.serializers import BorrowedBooksSerializer
from orders.models import BorrowedBooks


class BorrowedBooksModelViewSet(ModelViewSet):
    """a model view set for BorrowedBooks Model"""

    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
