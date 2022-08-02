from django.test import LiveServerTestCase, TestCase
from django.contrib.auth import get_user_model
from .models import User


class AuthTests(TestCase):
    def test_user_model(self):
        self.assertEqual(get_user_model(), User)

