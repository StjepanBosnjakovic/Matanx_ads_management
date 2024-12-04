# main_app/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import AdvertisementCampaign
from django.forms.widgets import CheckboxSelectMultiple, NumberInput
from datetime import timedelta




class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class AdvertisementCampaignForm(forms.ModelForm):
    min_time_between_runs = forms.IntegerField(
        label='Minimum Time Between Runs (in hours)',
        min_value=0,
        initial=1
    )

    class Meta:
        model = AdvertisementCampaign
        fields = [
            'name', 'description', 'city_areas', 'max_runnings', 'max_budget',
            'max_parallel_runs', 'min_time_between_runs', 'media_asset'
        ]
        widgets = {
            'city_areas': forms.CheckboxSelectMultiple(),
        }

    def clean_min_time_between_runs(self):
        hours = self.cleaned_data['min_time_between_runs']
        return timedelta(hours=hours)
    
    def get_estimated_cost(self):
        # Implement logic to estimate cost based on campaign settings
        # For simplicity, return a placeholder value
        return 100.00  # Replace with actual estimation logic
