from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password1', widget=forms.PasswordInput(attrs={'class': 'form-input pass', 'id': 'pass1'}))
    password2 = forms.CharField(label='Password2', widget=forms.PasswordInput(attrs={'class': 'form-input pass', 'id': 'pass2'}))
    field_order = ['username', 'password1', 'password2']

    class Meta:
        model = User
        fields = {'username', 'password1', 'password2'}


class AuthenticationFormPers(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-input pass', 'id': 'pass1'}))
    field_order = ['username', 'password']

    class Meta:
        model = User
        fields = {'username', 'password'}


class ProfileDate(forms.ModelForm):
    user_name = forms.CharField(label='User Name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    avatar = forms.ImageField(label='Profile Photo', widget=forms.FileInput(attrs={'class': 'avatar_in'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_status'].empty_label = "Default"
        self.fields['user_status'].label = "User Status"
        self.fields['user_status'].widget.attrs = {'class': 'form-select'}



    class Meta:
        model = UserProfile
        fields = ['user_name', 'user_status', 'avatar']

