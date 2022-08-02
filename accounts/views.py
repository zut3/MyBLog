from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def register(request, email: str):
    user = authenticate(email=email)
    login(request, user=user)
    return HttpResponse("ok!")


def test(request):
    return HttpResponse(str(request.user.is_authenticated))


