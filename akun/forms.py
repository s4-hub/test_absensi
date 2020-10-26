from django import forms
from dal import autocomplete
from django.contrib.auth.models import User

from .models import Profil


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfilEditForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ('user', 'photo', 'nama', 'npk')

        widgets = {
            'user': autocomplete.ModelSelect2(
                url='akun:user-autocomplete'),

            'photo': forms.FileInput(
                attrs={'class': 'form-control'}),
            'nama': forms.TextInput(
                attrs={'class': 'form-control'}),
            'npk': forms.TextInput(
                attrs={'class': 'form-control'}),
        }
