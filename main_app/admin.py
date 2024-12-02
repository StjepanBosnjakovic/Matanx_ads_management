from django.contrib import admin

# Register your models here.
from .models import CityArea, AdvertisementCampaign
admin.site.register(CityArea)
admin.site.register(AdvertisementCampaign)