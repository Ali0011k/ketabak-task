from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.api.v1.views import *


app_name = "api-v1"

router = DefaultRouter()


router.register("users", UserModelViewSet, basename="users")

urlpatterns = [
    path("", include(router.urls)),
    path("verify/<str:token>/", VerifyUserApiView.as_view(), name="verify-user"),
]
