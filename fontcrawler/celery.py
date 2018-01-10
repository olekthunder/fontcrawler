from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from .settings import INSTALLED_APPS

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fontcrawler.settings')

app = Celery('main')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: INSTALLED_APPS)
