from django.db import models


class Book(models.Model):
    """this is Book model"""

    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    cover_image = models.ImageField(upload_to="images")

    def short_description(self):
        return str(self.description[0:10])

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Books"
        verbose_name = "Book"
        verbose_name_plural = "Books"
