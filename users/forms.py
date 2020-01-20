
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model=CustomUser
        fields=('username','email')
        help_texts={
            'username':None,
            'email':None,
        }




class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        model=CustomUser
        fields=('username','email')