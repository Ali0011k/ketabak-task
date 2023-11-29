from django.contrib import admin
from orders.models import BorrowedBooks


@admin.register(BorrowedBooks)
class BorrowedBooksAdmin(admin.ModelAdmin):
    list_display = ["user", "received_at", "validity_at"]
    list_filter = ["received_at", "validity_at"]
    fieldsets = (
        ("General", {"fields": ("user", "address")}),
        ("Books", {"fields": ("books", "validity_at")}),
    )
    add_fieldsets = (
        ("General", {"fields": ("user", "address")}),
        ("Books", {"fields": ("books",)}),
        ("Important Dates", {"fields": ("validity_at",)}),
    )
