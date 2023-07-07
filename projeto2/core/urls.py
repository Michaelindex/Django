from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('core/', include('core.urls')),
]
