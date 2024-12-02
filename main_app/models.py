# main_app/models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from datetime import timedelta

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
