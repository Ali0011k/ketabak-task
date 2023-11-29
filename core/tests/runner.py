from django.test.runner import DiscoverRunner as BaseRunner
from django.utils import timezone
from django.contrib.auth.models import User
from decouple import config
from PIL import Image
from io import BytesIO
from books.models import Book
from orders.models import BorrowedBooks
import requests


# for unit test
class TestRunnerMixin(object):
    """a custom test mixin for all tests"""

    def setup_databases(self, *args, **kwargs):
        temp_return = super(TestRunnerMixin, self).setup_databases(*args, **kwargs)
        # * custom commands
        url = "https://img.freepik.com/free-photo/digital-painting-mountain-with-colorful-tree-foreground_1340-25699.jpg"
        image_request = requests.get(url=url)
        image = Image.open(BytesIO(image_request.content))
        book = Book.objects.create(
            name="Test Book",
            author="Test Books Author",
            price=10000,
            description="This is a book for testing book model",
            cover_image=image.info.get("filename"),
        )
        user = User.objects.create_user(
            username=config("USERNAME", cast=str),
            email=config("EMAIL", cast=str),
            password=config("DJANGO_SUPERUSER_PASSWORD", cast=str),
        )
        borrowedbook = BorrowedBooks.objects.create(
            user=user,
            address="test address",
        )
        borrowedbook.books.add(book)

        return temp_return

    def teardown_databases(self, *args, **kwargs):
        return super(TestRunnerMixin, self).teardown_databases(*args, **kwargs)


class TestRunner(TestRunnerMixin, BaseRunner):
    """a custom test runner"""

    pass
