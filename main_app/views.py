from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home(request):
    return render(request, 'main_app/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'main_app/register.html', {'form': form})
