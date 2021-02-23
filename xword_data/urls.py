""" URL patterns for xword_data app"""

from dajngo.urls import path

from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]