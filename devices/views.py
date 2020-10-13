from django.shortcuts import render

# Create your views here.\


def all_devices(request):
    return render(request, "devices/all_devices.html")


def add_device(request):
    return render(request, "devices/add_device.html")


def discover_devices(request):
    return render(request, "devices/discover_devices.html")


def manage_devices(request):
    return render(request, "devices/manage_devices.html")


