from django.contrib import admin
from books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """admin class for Book model"""

    list_display = ["name", "author", "price"]
    list_filter = ["price"]
    fieldsets = (
        ("General", {"fields": ("name", "author", "price")}),
        ("More Info", {"fields": ("description", "cover_image")}),
    )
    add_fieldsets = (
        ("General", {"fields": ("name", "author", "price")}),
        ("More Info", {"fields": ("description", "cover_image")}),
    )
