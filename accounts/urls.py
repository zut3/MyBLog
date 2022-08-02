from django.urls import path
from . import views

urlpatterns = [
    path('registration/<str:email>', views.register),
    path('test', views.test)
]
