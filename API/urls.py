"""NetDevOps URL Configuration

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
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from .views import CredentialViewSet, DeviceViewSet, ConnectionProtocolViewSet, TemplateViewSet, TemplateGroupViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'user', UserViewSet)
router.register(r'credential', CredentialViewSet)
router.register(r'device', DeviceViewSet)
router.register(r'template', TemplateViewSet)
router.register(r'template_group', TemplateGroupViewSet)
router.register(r'connection_protocol', ConnectionProtocolViewSet)


# app_name = 'API'
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('openapi', get_schema_view(
        title="CAPSNET - NetDevOps Tool",
        description="API Documentation",
        version="1.0.0"
    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]
