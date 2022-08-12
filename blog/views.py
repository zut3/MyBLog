from django.shortcuts import render
from services.mailing import send_mail
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def send_email(request):
    send_mail('lallala', 'lalallala', ['z.gl3b@yandex.ru'])
    return HttpResponse('ok!')
