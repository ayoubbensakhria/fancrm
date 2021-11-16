from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _

from .models import CustomUser

# inherit from UserCreationForm to restyle the form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=50,
                             widget=(forms.TextInput(attrs={'class': 'form-control'})))
    password1 = forms.CharField(label=_('Password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'})))
    password2 = forms.CharField(label=_('Password Confirmation'), widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomUserAuthForm(AuthenticationForm):
    username = forms.EmailField(max_length=50,
                             widget=(forms.TextInput(attrs={'class': 'form-control'})))
    password = forms.CharField(label=_('Password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'})))

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'})))
    new_password1 = forms.CharField(label=_('New password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'})))
    new_password2 = forms.CharField(label=_('New password confirmation'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'})))
    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=50,
                             widget=(forms.TextInput(attrs={'class': 'form-control'})))