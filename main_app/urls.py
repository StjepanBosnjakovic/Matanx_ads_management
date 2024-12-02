from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Home view
    path('', views.home, name='home'),
    # Registration view
    path('register/', views.register, name='register'),
    # Login view
    path('login/', auth_views.LoginView.as_view(template_name='main_app/login.html'), name='login'),
    # Logout view
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='main_app/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main_app/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='main_app/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='main_app/password_reset_complete.html'), name='password_reset_complete'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('campaign/create/', views.create_campaign, name='create_campaign'),
    path('campaign/delete/<int:campaign_id>/', views.delete_campaign, name='delete_campaign'),
    path('campaign/edit/<int:campaign_id>/', views.edit_campaign, name='edit_campaign'),  # If implementing edit

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
