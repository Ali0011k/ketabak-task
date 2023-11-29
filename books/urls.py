from django.urls import path, include


app_name = "books"
urlpatterns = [path("api/v1/", include("books.api.v1.urls"))]
