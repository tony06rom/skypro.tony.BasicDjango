from django import forms
from django.contrib.auth.forms import UserCreationForm
from catalog.forms import StyleFormMixin
from users.models import CustomUser


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password1', 'password2', 'first_name', 'last_name', 'country', 'phone', 'avatar']
