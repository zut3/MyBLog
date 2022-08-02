from django.urls import path
from . import views

urlpatterns = [
    path('registration/<str:email>', views.register),
    path('login/<uuid:uid>', views.confirm),
    path('test', views.test)
]
