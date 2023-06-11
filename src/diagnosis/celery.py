import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "diagnosis.settings.development")
app = Celery("diagnosis")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
