from celery import Celery
from celery.schedules import crontab
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("hello world")


app.conf.beat_schedule = {
    "send-end-email-every-day": {
        "task": "send_end_email",
        "schedule": crontab(hour=12, minute=0),
    },
}
