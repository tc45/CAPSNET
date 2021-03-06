from django.shortcuts import render, redirect, get_object_or_404
from .models import Device, SeedDevice
from appsettings.models import Credential
from ipaddress import ip_address, IPv4Address
from .forms import SeedDeviceForm
from django.contrib.auth.decorators import login_required

# Create your views here.\


@login_required()
def all_devices(request):
    devices = Device.objects.all()
    credentials = Credential.objects.all()
    page = 'devices'
    pagedetail = page + '.all_devices'
    context = {
        'devices': devices,
        'credentials': credentials,
        'page': page,
        'pagedetail': pagedetail
    }
    return render(request, "devices/all_devices.html", context)


@login_required()
def add_device(request):
    page = 'devices'
    pagedetail = page + '.add_device'
    context = {
        'form': SeedDeviceForm,
        'page': page,
        'pagedetail': pagedetail
    }
    if request.method == 'GET':
        return render(request, 'devices/add_device.html', context)
    else:
        # Create error based on validation of IP/hostname.
        error = ""
        # track for a valid return.  if valid, then save to database.
        valid_return = False


        # Get the list of devices so we can compare the IP to see if it already exists.
        devices = Device.objects.all()
        seeds = SeedDevice.objects.all()
        returned_seed = request.POST['seed_host_or_ip']

        if validIPAddress(returned_seed) == "IPv4":
            error = returned_seed + ' is a valid IPv4 address. Adding to discovery queue.'
            valid_return = True
        elif validIPAddress(returned_seed) == "Invalid":
            error = "Invalid IP Address entered. Enter a valid host or IP address to continue."
            protocol, ip_add, cidr = validCIDR(returned_seed)
            if protocol is not ["", " ", None]:
                valid_return = True
                error = returned_seed + ' is a valid CIDR format ' + protocol + ' address. Adding to discovery queue.'
        elif returned_seed is ["", " ", None]:
            error = "Host is blank. Enter a valid host or IP address to continue."
        elif returned_seed is not ["", " ", None]:
            error = "Host " + returned_seed + validIPAddress(returned_seed) +' is not in the database. Adding to discovery queue.'
            valid_return = True
        else:
            error = "Skipping hostname: " + validIPAddress(returned_seed)

        for device in devices:
            if device.management_ip == returned_seed:
                error = 'Duplicate management IP: ' + returned_seed + \
                        '.  This device has already been added.  Add a device that ' \
                        'isn''t in the database and try again.'
                valid_return = False
            if device.hostname == returned_seed:
                error = 'Duplicate hostname ' + returned_seed + \
                        '.  This device has already been added.  Add a device that ' \
                        'isn''t in the database and try again.'
                valid_return = False

        for seed in seeds:
            if seed.seed_host_or_ip == returned_seed:
                error = 'Duplicate added: ' + returned_seed + \
                        '.  This device/subnet has already been added.  Add a device or subnet that ' \
                        'isn''t in the database and try again.'
                valid_return = False


        # If we got IPv4, IPv6 or CIDR format return and no error
        if valid_return:
            # Get form from POST
            form = SeedDeviceForm(request.POST)
            # Put this in DB, but don't save.
            newform = form.save(commit=False)
            # Add user info to the form before saving.
            newform.user = request.user
            # Save the database if we received a valid input in the form.
            newform.save()
        # Return user to add_device page, with the form, and any errors(or successes)
        context['error'] = error
        return render(request, 'devices/add_device.html', context)


@login_required()
def discover_devices(request):
    if request.method == 'GET':
        seeds = SeedDevice.objects.all()
        page = 'devices'
        pagedetail = page + '.discover_devices'
        context = {
            'seeds': seeds,
            'page': page,
            'pagedetail': pagedetail
        }
        return render(request, "devices/discover_devices.html", context)



@login_required()
def discover_details(request, seeddevice_pk):
    if request.method == 'GET':
        # Show individual seed details
        seed = get_object_or_404(SeedDevice, pk=seeddevice_pk)
        credentials = Credential.objects.all()
        context = {
            'seed': seed,
            'credentials': credentials
        }
        return render(request, 'devices/discover_details.html', context)


@login_required()
def discover_details_edit(request, seeddevice_pk):
    if request.method == 'GET':
        # Show individual seed details
        seed = get_object_or_404(SeedDevice, pk=seeddevice_pk)
        credentials = Credential.objects.all()
        context = {
            'seed': seed,
            'credentials': credentials
        }
        return render(request, 'devices/discover_details_edit.html', context)


@login_required()
def manage_devices(request):
    page = 'devices'
    pagedetail = page + '.manage_devices'
    context = {
        'page': page,
        'pagedetail': pagedetail
    }
    return render(request, "devices/manage_devices.html", context)


@login_required()
def device_details(request, device_pk):
    # Show individual device details
    device = get_object_or_404(Device, pk=device_pk)

    page = 'devices'
    pagedetail = page + '.all_devices'
    context = {
        'device': device,
        'page': page,
        'pagedetail': pagedetail
    }

    if request.method == 'GET':
        return render(request, 'devices/device_details.html', context)


def validIPAddress(IP: str) -> str:
    try:
        return "IPv4" if type(ip_address(IP)) is IPv4Address else "IPv6"
    except ValueError:
        return "Invalid"


def validCIDR(IP : str) -> str:
    valid_return = False
    output = {}

    # Replace backslash with forward slash
    value = IP.replace("\\", "/")

    if "/" in value:
        # Split string into CIDR and IP
        split = value.split("/")
        output['ip_address'] = split[0]
        output['cidr'] = split[1]
        # Check if first of string has IPv4 address
        if validIPAddress(output['ip_address']) == "IPv4":
            # Check if back of string has d digit less than or equal to 32
            if int(output['cidr']) <= 32:
                valid_return = True
                output['protocol'] = "IPv4"
        # Check if first of string has IPv4 address
        elif validIPAddress(output['ip_address']) == "IPv6":
            # Check if back of string has d digit less than or equal to 32
            if int(output['cidr']) <= 128:
                valid_return = True
                output['protocol'] = "IPv6"

    if valid_return:
        return output
    else:
        return False





