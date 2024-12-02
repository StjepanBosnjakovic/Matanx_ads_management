from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm, AdvertisementCampaignForm
from django.contrib.auth.decorators import login_required
from .models import AdvertisementCampaign
from django.contrib import messages



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
    return render(request, 'main_app/create_campaign.html', {'form': form})

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
    return render(request, 'main_app/edit_campaign.html', {'form': form})


@login_required
def delete_campaign(request, campaign_id):
    campaign = AdvertisementCampaign.objects.get(id=campaign_id, user=request.user)
    if request.method == 'POST':
        campaign.delete()
        return redirect('dashboard')
    return render(request, 'delete_campaign.html', {'campaign': campaign})