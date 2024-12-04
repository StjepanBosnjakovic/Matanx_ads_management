# main_app/models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from datetime import timedelta
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import secrets

def generate_token():
    return secrets.token_hex(20)

class CityArea(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class AdvertisementCampaign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    city_areas = models.ManyToManyField(CityArea)
    max_runnings = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    max_budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    max_parallel_runs = models.PositiveIntegerField(blank=True, null=True)
    min_time_between_runs = models.DurationField(default=timedelta(hours=1))
    media_asset = models.FileField(upload_to='media_assets/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ExternalSystem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    token = models.CharField(max_length=40, unique=True, default=generate_token)

    def __str__(self):
        return self.name
    
class AdvertisementRunHistory(models.Model):
    campaign = models.ForeignKey(AdvertisementCampaign, on_delete=models.CASCADE)
    run_time = models.DateTimeField()
    duration = models.PositiveIntegerField(default=0)  # Duration in seconds
    city_area = models.ForeignKey(CityArea, on_delete=models.CASCADE)
    external_system = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    additional_data = models.JSONField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.campaign.name} run at {self.run_time}"

    
class PricingRule(models.Model):
    name = models.CharField(max_length=100)
    rate_per_second = models.DecimalField(max_digits=10, decimal_places=4)  # Rate in cents per second
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    days_of_week = ArrayField(
        models.IntegerField(),
        size=7,
        null=True,
        blank=True,
        help_text='Days of the week as integers: 0 (Monday) - 6 (Sunday)'
    )
    city_areas = models.ManyToManyField('CityArea', blank=True)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Pricing Rule'
        verbose_name_plural = 'Pricing Rules'

    def __str__(self):
        return self.name