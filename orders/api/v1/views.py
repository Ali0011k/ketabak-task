from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import *
from books.api.permissions import IsAdminOrReadOnly
from orders.api.v1.serializers import BorrowedBooksSerializer
from orders.api.paginations import BorrowedBooksPagination
from orders.models import BorrowedBooks

class BorrowedBooksModelViewSet(ModelViewSet):
    """a model view set for BorrowedBooks Model"""

    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    pagination_class = BorrowedBooksPagination

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
