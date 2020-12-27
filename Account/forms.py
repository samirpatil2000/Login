from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

class userRegisterFrom(UserCreationForm):
    email = forms.EmailField(help_text='Enter your email address')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
