from django.urls import path

from . import views

urlpatterns = [
    path('',views.dashBoard, name='dashboard'),
    path('login', views.login, name='login'),
    path('callback',views.callback, name='callback'),
]