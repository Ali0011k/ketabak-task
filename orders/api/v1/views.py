from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import *
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from books.api.permissions import IsAdminOrReadOnly
from orders.api.v1.serializers import *
from orders.models import BorrowedBooks


class BorrowedBooksModelViewSet(ModelViewSet):
    """a model view set for BorrowedBooks Model"""

    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["user"]
    ordering_fields = ["id", "received_at", "validity_at"]
    search_fields = ["user"]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return (
                BorrowedBooks.objects.all()
                if user.is_staff or user.is_superuser
                else BorrowedBooks.objects.filter(user=user)
            )
        else:
            return BorrowedBooks.objects.none()

    def get_serializer_class(self, *args, **kwargs):
        if self.action in ["list", "retrieve"]:
            return BorrowedBooksGetActionSerializer
        else:
            return self.serializer_class
