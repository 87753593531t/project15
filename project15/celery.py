import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project15.settings')
celery_app = Celery('project15')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()