from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class CreateUserForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username', 'emali', 'password1', 'password2']