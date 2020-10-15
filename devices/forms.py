from django.forms import ModelForm
from .models import Device, Credential


class AddNewDeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = ['management_ip', 'hostname']

