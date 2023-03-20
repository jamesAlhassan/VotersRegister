from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=200)
    last_name= forms.CharField(max_length=200)
  
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("username", "first_name","last_name", "email")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name","email")
