from django.contrib.auth.models import AbstractUser
from django.db import models
from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    """custom user with an exrta field"""

    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username
