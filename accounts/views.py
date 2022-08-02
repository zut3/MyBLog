from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Token


def register(request, email: str):
    token = Token.objects.get_or_create(email=email)[0]
    return HttpResponse(token.uid)


def confirm(request, uid: str):
    user = authenticate(request, uid=uid)
    login(request, user)
    return HttpResponse('ok!')


def test(request):
    return HttpResponse(request.user.is_authenticated)


