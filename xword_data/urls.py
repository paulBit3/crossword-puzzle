""" URL patterns for xword_data app"""

from django.urls import path
from django.contrib.auth import views as auth_views


from .forms import AuthenticationForm

from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

     # authentication and authorization
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html',
        authentication_form= AuthenticationForm), name='login'),
    path('accounts/join/', views.join, name='join'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]