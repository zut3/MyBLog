from config.celery import app
from services.mailing import send_mail
from .models import BlogItem
from django.contrib.auth import get_user_model

User = get_user_model()


@app.task
def send_notification_mail_about_new_article():
    """Celery task. Присылает письмо о новой статье всем подписавшися пользователям. Not implemented!"""
    users_email = [user.email for user in User.objects.all()]
    not_notified_articles = BlogItem.objects.exclude(notified=False)
    print(not_notified_articles)
    print(users_email)





