from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Token
from services.mailing import send_mail


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        token = Token.objects.get_or_create(email=email)[0]
        url = reverse('confirm', kwargs={'uid': token.uid})
        send_mail('Confirm your email', request.build_absolute_uri(url), [email])
        return render(request, 'auth/registration.html', {'url': request.build_absolute_uri(url)})


def confirm(request, uid: str):
    user = authenticate(request, uid=uid)
    login(request, user)
    return HttpResponse('ok!')


def test(request):
    return HttpResponse(request.user.is_authenticated)


def user_page(request):
    return render(request, 'auth/user.html')


def logout_view(request):
    logout(request)
    return redirect('home')
