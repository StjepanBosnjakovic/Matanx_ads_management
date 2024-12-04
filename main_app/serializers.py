from rest_framework import serializers
from .models import AdvertisementRunHistory, AdvertisementCampaign, CityArea

class AdvertisementRunHistorySerializer(serializers.ModelSerializer):
    campaign_id = serializers.IntegerField()
    city_area_id = serializers.IntegerField()
    duration = serializers.IntegerField(required=True, help_text='Duration in seconds')

    class Meta:
        model = AdvertisementRunHistory
        fields = ['campaign_id', 'run_time', 'city_area_id', 'duration', 'external_system', 'additional_data']

    def create(self, validated_data):
        campaign_id = validated_data.pop('campaign_id')
        city_area_id = validated_data.pop('city_area_id')

        campaign = AdvertisementCampaign.objects.get(id=campaign_id)
        city_area = CityArea.objects.get(id=city_area_id)

        return AdvertisementRunHistory.objects.create(
            campaign=campaign,
            city_area=city_area,
            **validated_data
        )
