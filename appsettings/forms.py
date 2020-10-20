from django.forms import ModelForm
from .models import Credential
from appsettings.models import Credential, CustomerGeneral


class AddVTYCredentialsForm(ModelForm):
    class Meta:
        model = Credential
        fields = [
            'username',
            'password',
            'enable_pass',
            'description',
            'changed',
            'user'
        ]


class CustomerGeneralForm(ModelForm):
    class Meta:
        model = CustomerGeneral
        fields = [
            'CustomerName',
            'CustomerDescription',
            'primaryContactFirstName',
            'primaryContactLastName',
            'primaryContactEmail',
            'primaryContactCellPhone',
            'primaryContactWorkPhone',
            'primaryContactAddress1',
            'primaryContactAddress2',
            'primaryContactCity',
        ]