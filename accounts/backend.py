from django.contrib.auth.backends import BaseBackend
from .models import User


class Backend(BaseBackend):

    def authenticate(self, request, email=None):
        if email is None:
            raise ValueError("email")

        try:
            user = User.objects.get(email=email)
            return user
        except User.DoesNotExist:
            return User.objects.create(email=email)

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
