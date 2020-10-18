"""CAPSNET URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views
from django.conf import settings

app_name = 'devices'

urlpatterns = [
    path('', views.all_devices, name="all_devices"),
    # Paths for the devices/device/ path
    path('device/<int:device_pk>/', views.device_details, name='device_details'),
    path('add/', views.add_device, name="add_device"),
    # Paths for the devices/discover/ path
    path('discover/', views.discover_devices, name="discover_devices"),
    path('discover/<int:seeddevice_pk>/', views.discover_details, name='discover_details'),
    path('discover/<int:seeddevice_pk>/edit', views.discover_details_edit, name='discover_details_edit'),
    # Paths for the devices/manage/ path
    path('manage/', views.manage_devices, name="manage_devices"),
]
