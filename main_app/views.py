from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm, AdvertisementCampaignForm
from django.contrib.auth.decorators import login_required
from .models import AdvertisementCampaign, AdvertisementRunHistory
from django.contrib import messages
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import AdvertisementRunHistorySerializer
from .authentication import ExternalSystemAuthentication
from rest_framework.permissions import IsAuthenticated



def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally, you can send a confirmation email here
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    campaigns = AdvertisementCampaign.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'campaigns': campaigns})

@login_required
def create_campaign(request):
    if request.method == 'POST':
        form = AdvertisementCampaignForm(request.POST, request.FILES)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.user = request.user
            campaign.save()
            form.save_m2m()  # Save many-to-many relationships
            messages.success(request, 'Campaign created successfully!')
            return redirect('dashboard')
    else:
        form = AdvertisementCampaignForm()
    return render(request, 'create_campaign.html', {'form': form})

@login_required
def edit_campaign(request, campaign_id):
    campaign = get_object_or_404(AdvertisementCampaign, id=campaign_id, user=request.user)
    if request.method == 'POST':
        form = AdvertisementCampaignForm(request.POST, request.FILES, instance=campaign)
        if form.is_valid():
            form.save()
            messages.success(request, 'Campaign updated successfully!')
            return redirect('dashboard')
    else:
        form = AdvertisementCampaignForm(instance=campaign)
    return render(request, 'edit_campaign.html', {'form': form})


@login_required
def delete_campaign(request, campaign_id):
    campaign = AdvertisementCampaign.objects.get(id=campaign_id, user=request.user)
    if request.method == 'POST':
        campaign.delete()
        return redirect('dashboard')
    return render(request, 'delete_campaign.html', {'campaign': campaign})

@login_required
def campaign_run_history(request, campaign_id):
    campaign = get_object_or_404(AdvertisementCampaign, id=campaign_id, user=request.user)
    run_history = AdvertisementRunHistory.objects.filter(campaign=campaign).order_by('-run_time')
    return render(request, 'campaign_run_history.html', {'campaign': campaign, 'run_history': run_history})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([ExternalSystemAuthentication])
def advertisement_run_history_create(request):
    serializer = AdvertisementRunHistorySerializer(data=request.data)
    if serializer.is_valid():
        campaign_id = serializer.validated_data['campaign_id']
        city_area_id = serializer.validated_data['city_area_id']
        run_time = serializer.validated_data['run_time']
        duration = serializer.validated_data.get('duration', 0)  # Assuming duration is provided

        campaign = AdvertisementCampaign.objects.get(id=campaign_id)
        city_area = CityArea.objects.get(id=city_area_id)

        # Calculate cost
        cost = calculate_ad_run_cost(campaign, city_area, run_time, duration)

        run_history = serializer.save(
            campaign=campaign,
            city_area=city_area,
            cost=cost,
            external_system=request.user.username
        )
        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
