import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery("config")
app.config_from_object("django.conf:settings")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'notify': {
        'task': 'blog.tasks.send_notification_mail_about_new_article',
        'schedule': crontab(minute='0', hour='0')
    }
}
