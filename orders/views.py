from django.http import HttpResponse
from core.celery import debug_task


def test(request):
    debug_task.delay()
    return HttpResponse("ok")
