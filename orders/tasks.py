from django.core.mail import send_mail
from celery import shared_task
from orders.models import BorrowedBooks
from django.utils import timezone


@shared_task(name="send_got_email")
def send_got_email_task(email, *books):
    """a task for sending email for when got books"""
    book_names = []
    for book in books:
        book_names.append(book)
    send_mail(
        "got books",
        f"you got these books from ketabak  \n{', '.join(book_names)}",
        "ketabak@gmail.com",
        [email],
        fail_silently=True,
    )


@shared_task(name="send_end_email")
def send_end_email():
    """send an email when validity time is over"""
    two_days_ago = timezone.now() - timezone.timedelta(days=2)

    all_borrowedbooks = BorrowedBooks.objects.all()
    for borrowedbook in all_borrowedbooks:
        if borrowedbook.validity_at.day == two_days_ago.day:
            books = borrowedbook.books.all()
            book_names = [book.name for book in books]

            send_mail(
                "Reminder: Return Borrowed Books",
                f"You borrowed the following books from ketabak. Please return them:\n{', '.join(book_names)}",
                "ketabak@gmail.com",
                [borrowedbook.user.email],
                fail_silently=True,
            )
