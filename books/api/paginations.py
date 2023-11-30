from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class CustomLimitOffsetPagination(LimitOffsetPagination):
    """a pagination class for BookModelViewSet"""
    def get_paginated_response(self, data):
        return Response(data)
