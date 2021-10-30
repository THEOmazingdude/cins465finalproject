from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        "title": "cins465 Final Project",
        "body": "This is a website."
    }
    return render(request, "index.html", context = context)
#end index