import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fogstreamtest.settings')

app = Celery('fogstreamtest', broker='redis://127.0.0.1:6379')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
