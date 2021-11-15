from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomPasswordResetForm, CustomUserAuthForm, CustomPasswordChangeForm
from django.views.generic.base import TemplateView

urlpatterns = [
    # Work With Django User Management
    url(r"^dashboard/", views.dashboard, name="dashboard"),
    #url(r"^accounts/", include("django.contrib.auth.urls")),
    path('accounts/register/', views.register,name="register"),
    #path('accounts/login/', views.signin,name="login"),
    path('accounts/login/', auth_views.LoginView.as_view(form_class=CustomUserAuthForm),name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(),name="logout"),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(form_class=CustomPasswordResetForm), name="password_reset"),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(form_class=CustomPasswordChangeForm), name="change_password"),
    path('accounts/', include('allauth.urls')),
]