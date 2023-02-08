from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label = "이메일")

    class Meta:
        model = User
        #password1, password2 내용은 동일해야한다.
        fields = ["username", "password1", "password2", "email"]

