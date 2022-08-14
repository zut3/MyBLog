from config.celery import app
from services.mailing import send_html_template
from .models import BlogItem
from django.contrib.auth import get_user_model
from pathlib import Path

User = get_user_model()


@app.task
def send_notification_mail_about_new_article():
    """Celery task. Присылает письмо о новой статье всем подписавшися пользователям. Not implemented!"""
    users_email = [user.email for user in User.objects.filter(subscribed=True)]
    new_articles = list(BlogItem.objects.filter(notified=False))
    if not new_articles:
        return
    send_html_template(subject="New articles", template_path=Path("mailing/new_article.html"),
                       context={"articles": new_articles}, to=users_email)

    for article in new_articles:
        article.notified = True
        article.save()
