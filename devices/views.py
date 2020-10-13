from django.shortcuts import render
from .models import Device
from settings.models import Credential

# Create your views here.\


def all_devices(request):
    devices = Device.objects.all()
    credentials = Credential.objects.all()
    return render(request, "devices/all_devices.html", {'devices': devices, 'credentials': credentials})


def add_device(request):
    return render(request, "devices/add_device.html")


def discover_devices(request):
    return render(request, "devices/discover_devices.html")


def manage_devices(request):
    return render(request, "devices/manage_devices.html")


