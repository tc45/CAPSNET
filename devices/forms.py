from django.forms import ModelForm
from .models import SeedDevice
from appsettings.models import Credential


class SeedDeviceForm(ModelForm):
    class Meta:
        model = SeedDevice
        fields = ['seed_host_or_ip', 'credential']

