from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)


    class Meta:
        model = User    #TODO: Change to create a profile model
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2']