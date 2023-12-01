from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.api.v1.views import *

router = DefaultRouter()


router.register("users", UserModelViewSet, basename="users")
router.register("permissions", PermissionModelViewSet, basename="permissions")
router.register("groups", GroupModelViewSet, basename="groups")


urlpatterns = [
    path("", include(router.urls)),
]