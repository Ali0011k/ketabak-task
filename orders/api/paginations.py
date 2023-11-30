from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

class BorrowedBooksPagination(LimitOffsetPagination):
    
    def get_paginated_response(self, data):
        return Response(data)