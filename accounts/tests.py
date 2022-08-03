from django.test import LiveServerTestCase
from django.contrib.auth import get_user_model
from .models import User


class AuthTests(LiveServerTestCase):
    def test_user_model(self):
        self.assertEqual(get_user_model(), User)

    def test_can_register(self):
        url = self.live_server_url + '/auth/registration/mail@mail.com'
        uid = str(self.client.get(url).content.decode('ascii'))
        self.assertTrue(uid)
        url = self.live_server_url + '/auth/login/' + uid
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        


