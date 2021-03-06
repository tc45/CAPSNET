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
from dashboard import views as dashboard_views

admin.site.site_header = "CAPSNET - Admin Portal"
admin.site.site_title = "CAPSNET - Admin Portal"
admin.site.index_title = "Admin Page"

urlpatterns = [
    path('admin/', admin.site.urls),

    #Auth
    path('signup/', dashboard_views.signupuser, name="signupuser"),
    path('logout/', dashboard_views.logoutuser, name="logoutuser"),
    path('login/', dashboard_views.loginuser, name="loginuser"),

    # API URLs
    path('api/', include('API.urls')),
    # Dashboard URLs
    path('', include('dashboard.urls')),
    # Devices URLs
    path('devices/', include('devices.urls')),
    # Templates URLs
    path('templates/', include('apptemplates.urls')),
    # Provisioning URLs
    path('provisioning/', include('provisioning.urls')),
    # Tools URLS
    path('tools/', include('tools.urls')),
    # Reports URLs
    path('reports/', include('reports.urls')),
    # Settings URLs
    path('settings/', include('appsettings.urls')),
]
