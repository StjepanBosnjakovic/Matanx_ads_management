from django.contrib import admin
from .models import CityArea, AdvertisementCampaign, ExternalSystem, AdvertisementRunHistory
from .models import PricingRule


admin.site.register(CityArea)
admin.site.register(AdvertisementCampaign)
admin.site.register(ExternalSystem)
admin.site.register(AdvertisementRunHistory)

@admin.register(PricingRule)
class PricingRuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate_per_second', 'is_default')
    list_filter = ('is_default', 'days_of_week')
    filter_horizontal = ('city_areas',)