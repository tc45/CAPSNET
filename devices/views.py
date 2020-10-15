from django.shortcuts import render, redirect, get_object_or_404
from .models import Device
from appsettings.models import Credential

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


def device_details(request, device_pk):
    # Show individual device details
    device = get_object_or_404(Device, pk=device_pk)
    if request.method == 'GET':
        return render(request, 'devices/device_details.html', {'device': device})


