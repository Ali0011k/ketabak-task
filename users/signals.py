from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


@receiver(post_save, sender=User)
def send_verification_email(sender, instance, created, *args, **kwargs):
    """a signal for sending verification email for user"""

    if created:
        url = settings.HOSTNAME
        user = instance
        token = RefreshToken.for_user(user).access_token
        url += reverse("users:api-v1:verify-user", kwargs={"token": str(token)})
        send_mail(
            "ketabak : verification email",
            f"palace activate your account form this url \n {url}",
            "ketabak@gmail.com",
            [instance.email],
            fail_silently=True,
        )
