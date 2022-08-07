from django.test import LiveServerTestCase
from django.contrib.auth import get_user_model
from .models import User
from unittest.mock import patch, MagicMock


class AuthTests(LiveServerTestCase):
    def test_user_model(self):
        self.assertEqual(get_user_model(), User)

    @patch('accounts.views.send_mail')
    def test_send_mail_after_registration(self, send_mail_mock: MagicMock):
        email = 'mail@mail.com'
        url = self.live_server_url + '/auth/registration'
        response = self.client.post(url, data={'email': email})
        self.assertEqual(response.status_code, 200)
        subject, body, to, *other = send_mail_mock.call_args[0]
        self.assertIn(email, to)


