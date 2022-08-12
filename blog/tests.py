from django.test import LiveServerTestCase
from accounts.models import Token


class BlogTests(LiveServerTestCase):

    def test_can_subscribe(self):
        token = Token.objects.create(email="mail@mail.com")
        success = self.client.login(uid=token.uid)
        self.assertTrue(success)
        response = self.client.get(self.live_server_url + "/subscribe")
        self.assertTrue(response.wsgi_request.user.subscribed)
