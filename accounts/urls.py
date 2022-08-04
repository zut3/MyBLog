from django.urls import path
from . import views

urlpatterns = [
    path('registration', views.register, name='register'),
    path('login/<uuid:uid>', views.confirm, name='confirm'),
    path('test', views.test)
]
