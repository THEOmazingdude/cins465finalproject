from django import forms
from django.core import validators
from django.core.validators import validate_unicode_slug
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as auth_user

from . import models

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        # validators=[must_be_unique]
    )

    class Meta:
        model = auth_user
        fields = (
            "username",
            "email",
            "password1",
            "password2"
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    #end save
#end reg form

def must_be_auth_user(value):
    entry = auth_user.objects.filter(username = value)
    if len(entry) == 0:
        raise forms.ValidationError("Players must be authenticated users")
    return value

def valid_winner(value):
    entry = auth_user.objects.filter(username = value)
    winner = value.upper()
    if len(entry) == 0 and winner != "DRAW":
        raise forms.ValidationError("Winner must be an authenticated user or 'draw'")
    return winner

class gameForm(forms.Form):
    white = forms.CharField(
        label = "White:",
        required = True,
        validators=[must_be_auth_user]
    )

    black = forms.CharField(
        label = "Black:",
        required = True,
        validators=[must_be_auth_user]
    )

    winner = forms.CharField(
        label = "Winner:",
        required = True,
        validators = [valid_winner]
    )

    def save(self):
        game_instance = models.game()
        game_instance.winner = self.cleaned_data["winner"].upper()
        game_instance.save()
        game_instance.players.add(models.auth_user.objects.get(username = self.cleaned_data["white"]))
        game_instance.players.add(models.auth_user.objects.get(username = self.cleaned_data["black"]))
        
        return game_instance

    