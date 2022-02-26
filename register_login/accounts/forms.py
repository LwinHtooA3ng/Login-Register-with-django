from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(min_length=4, max_length=30)
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'validate',}))
    class Meta:
        model = User
        fields = [
            'username',
            'email', 
            'password1',
            'password2',
        ]
