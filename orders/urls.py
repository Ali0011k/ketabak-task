from django.urls import path, include
from .views import *

app_name = "orders"

urlpatterns = [path("api/", include("orders.api.v1.urls")), path("test/", test)]
