from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders.api.v1.views import *

router = DefaultRouter()
router.register("borrowedbooks", BorrowedBooksModelViewSet, basename="borrowedbooks")

app_name = "api-v1"

urlpatterns = [path("", include(router.urls))]
