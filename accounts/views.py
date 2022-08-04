from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Token
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register(request):
    if request.method == 'POST':
        print(request.POST)
        email = request.POST['email']
        print(email)
        token = Token.objects.get_or_create(email=email)[0]
        url = reverse('confirm', kwargs={'uid': token.uid})
        return render(request, 'auth/registration.html', {'url': request.build_absolute_uri(url) }) 


def confirm(request, uid: str):
    user = authenticate(request, uid=uid)
    login(request, user)
    return HttpResponse('ok!')


def test(request):
    return HttpResponse(request.user.is_authenticated)


