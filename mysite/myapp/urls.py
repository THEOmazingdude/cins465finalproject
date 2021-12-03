from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index),
    path('play/', views.play),
    path('players/', views.players),
    path('players/<str:player>/', views.player),
    path('yourgames/', views.yourgames),
    path('login/', auth_views.LoginView.as_view()),
    path('register/', views.register),
    path('logout/', views.logout_view),
    path('chat/', views.chat_index, name = 'index'),
    path('chat/<str:room_name>/', views.room, name = 'room'),
]