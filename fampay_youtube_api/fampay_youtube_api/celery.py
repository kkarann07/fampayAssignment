import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fampay_youtube_api.settings')

app = Celery('fampay_youtube_api')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.beat_schedule = {
    'fetch_latest_videos': {
        'task': 'youtube_app.tasks.fetch_latest_videos',
        'schedule': crontab(minute='*/1'),
    },
}
app.autodiscover_tasks()