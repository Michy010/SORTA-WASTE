from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import CustomUser

class CustomUserForm (UserCreationForm):
    is_seller = forms.BooleanField (label='Are you a seller?', required=False)

    class Meta (UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'is_seller']