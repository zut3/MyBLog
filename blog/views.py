from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


@login_required
def subscribe(request):
    """подписывает пользователя к блогу. Обязательна регистрация."""
    user = request.user
    user.subscribed = True
    user.save()
    return HttpResponse('now you subscribed to blog!')
