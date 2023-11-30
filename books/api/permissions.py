from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """cheking user is admin or not"""

    def has_permission(self, request, view):
        return bool(request.user)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user.is_staff or request.user.is_superuser)
