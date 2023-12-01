from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings


User = get_user_model()


@receiver(post_save, sender=User)
def send_verification_email(sender, instance, created, *args, **kwargs):
    """a signal for sending verification email for user"""
    
    url = settings.HOSTNAME
    print(url)
    send_mail(
        "ketabak : verification email",
        "palace activate your account form this url",
        "ketabak@gmail.com",
        [instance.email],
        fail_silently=True
    )