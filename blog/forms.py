from django import forms
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Type your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Type your password'}))