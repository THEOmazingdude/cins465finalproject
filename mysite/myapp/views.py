from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from . import models
from . import forms


# Create your views here.

def index(request):
    context = {
        "title": "cins465 Final Project",
        "body": "Home Page"
    }
    return render(request, "board.html", context = context)
#end index

@login_required
def play(request):
    context = {
        "title": "play",
        "user": request.user.username
    }
    return render(request, "chat/index.html", context = context)
#end play

@login_required
def players(request):
    Player = get_user_model()
    player_list = Player.objects.all()
    context = {
        "title": "PLAYERS",
        "player_list": player_list,
    }
    return render(request, "players.html", context = context)
#end players

@login_required
def player(request, player):
    gamelist = models.game.objects.filter(players__username = player)
    context = {
        "title": player,
        "body": "Here are stats about " + player,
        "count": gamelist.count,
    }
    return render(request, "player.html", context = context)

@login_required
def yourgames(request):
    context = {
        "title": "your games",
        "body": "On this page you can see your stats for all of your games."
    }
    return render(request, "index.html", context = context)
#end yourgames

def register(request):
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect("/login/")
    else:
        form = forms.RegistrationForm()
    
    context = {
        "title": "Registration Page",
        "form": form
    }
    return render(request, "registration/register.html", context = context)
#end register

@login_required
def logout_view(request):
    logout(request)
    return redirect("/")
#end logout

def chat_index(request):
    user = request.user.username
    context = {
        "title": "Chat",
        "user": user
    }
    return render(request, "chat/index.html", context = context)
#edn chat index

def room(request, room_name):
    if request.method == "POST":
        form = forms.gameForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            form.save()
            form = forms.gameForm()
    else:
        form = forms.gameForm()

    context = {
        "room_name": room_name,
        "user": request.user.username,
        "form": form
    }
    return render(request, "chat/room.html", context = context)
#end room

