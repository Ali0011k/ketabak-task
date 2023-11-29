from django.urls import path, include


app_name = "books"
urlpatterns = [path("api/", include("books.api.v1.urls"))]
