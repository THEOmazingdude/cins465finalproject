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