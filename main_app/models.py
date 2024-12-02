# main_app/models.py
from django.db import models
from django.contrib.auth.models import User

class AdvertisementCampaign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add other fields as needed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
