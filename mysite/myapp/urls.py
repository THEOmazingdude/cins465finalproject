from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('play/', views.play),
    path('players/', views.players),
    path('yourgames/', views.yourgames)
]