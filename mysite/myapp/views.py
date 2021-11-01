from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        "title": "cins465 Final Project",
        "body": "Home Page"
    }
    return render(request, "index.html", context = context)
#end index

def play(request):
    context = {
        "title": "cins465 Final Project",
        "body": "This is where you can play games... hopefully."
    }
    return render(request, "index.html", context = context)
#end play

def players(request):
    context = {
        "title": "cins465 Final Project",
        "body": "List all players by username."
    }
    return render(request, "index.html", context = context)
#end players

def yourgames(request):
    context = {
        "title": "cins465 Final Project",
        "body": "On this page you can see your stats for all of your games."
    }
    return render(request, "index.html", context = context)
#end yourgames