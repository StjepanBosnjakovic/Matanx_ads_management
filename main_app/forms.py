# main_app/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import AdvertisementCampaign


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class AdvertisementCampaignForm(forms.ModelForm):
    class Meta:
        model = AdvertisementCampaign
        fields = ['name', 'description']
