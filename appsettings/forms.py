from django.forms import ModelForm
from .models import Credential
from appsettings.models import Credential


class AddVTYCredentialsForm(ModelForm):
    class Meta:
        model = Credential
        fields = ['username',
                  'password',
                  'enable_pass',
                  'description',
                  'changed',
                  'user'
                  ]
