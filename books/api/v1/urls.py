from django.urls import path, include
from books.api.v1.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("books", BookModelViewSet, basename="books")


app_name = "api-v1"
urlpatterns = [path("", include(router.urls))]
