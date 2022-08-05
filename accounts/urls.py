from django.urls import path
from . import views

urlpatterns = [
    path('registration', views.register, name='register'),
    path('login/<uuid:uid>', views.confirm, name='confirm'),
    path('logout', views.logout_view, name='logout'),
    path('test', views.test),
    path('user', views.user_page)
]
