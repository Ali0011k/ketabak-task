from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.utils.timezone import timedelta
from orders.models import BorrowedBooks
from orders.tasks import *


@receiver(post_save, sender=BorrowedBooks)
def update_validity_at(sender, instance, created, *args, **kwargs):
    """update validity date when this model is creating"""
    if created:
        if not instance.validity_at:
            instance.validity_at = instance.received_at + timedelta(days=2)
            instance.save()


def send_got_email(sender, instance, action, *args, **kwargs):
    """send an email for user when model is creating"""

    if action == "post_add":
        books = instance.books.all()
        book_names = []
        for book in books:
            book_names.append(book.name)

        send_got_email_task.delay(instance.user.email, *book_names)


m2m_changed.connect(send_got_email, sender=BorrowedBooks.books.through)
