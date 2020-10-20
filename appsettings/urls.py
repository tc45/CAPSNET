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

app_name = 'appsettings'

urlpatterns = [
    path('', views.settings_home, name="settings_home"),
    # VTY Pages
    path('vty/', views.addvtycredential, name="addvtycredential"),
    path('vty/<int:credential_pk>/edit', views.editvtycredential, name="editvtycredential"),
    path('vty/<int:credential_pk>/delete', views.deletevtycredential, name='deletevtycredential'),
    # SNMP Pages
    path('snmp/', views.addsnmpcredential, name="addsnmpcredential"),
    path('snmp/<int:snmp_pk>/edit', views.editsnmpcredential, name="editsnmpcredential"),
    path('snmp/<int:snmp_pk>/delete', views.deletesnmpcredential, name='deletesnmpcredential'),
]
