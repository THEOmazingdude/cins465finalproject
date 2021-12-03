from django.db import models
from django.contrib.auth.models import User as auth_user

# Create your models here.

class game(models.Model):
    players = models.ManyToManyField(auth_user)

    
