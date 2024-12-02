from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Home view
    path('', views.home, name='home'),
    # Registration view
    path('register/', views.register, name='register'),
    # Login view
    path('login/', auth_views.LoginView.as_view(template_name='main_app/login.html'), name='login'),
    # Logout view
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
