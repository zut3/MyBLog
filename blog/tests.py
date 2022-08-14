from django.test import LiveServerTestCase
from unittest.mock import patch, MagicMock
from accounts.models import Token, User
from .models import BlogItem
from . import tasks


class BlogTests(LiveServerTestCase):

    def test_can_subscribe(self):
        token = Token.objects.create(email="mail@mail.com")
        success = self.client.login(uid=token.uid)
        self.assertTrue(success)
        response = self.client.get(self.live_server_url + "/subscribe")
        self.assertTrue(response.wsgi_request.user.subscribed)

    def test_send_mail_about_new_article(self):
        mail = "mail@mail.com"
        User.objects.create(email=mail, subscribed=True)
        BlogItem.objects.create(title="lalala", text="## Hello")
        mock = MagicMock()
        tasks.send_html_template = mock
        tasks.send_notification_mail_about_new_article()
        mock.assert_called()
        self.assertIn(mail, mock.call_args.kwargs['to'])

