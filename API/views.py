from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import CredentialSerializer, DeviceSerializer, TemplateSerializer, TemplateGroupSerializer, \
    ConnectionProtocolSerializer, InventorySerializer, DeviceTypeSerializer
from apptemplates.models import Template, TemplateGroup
from appsettings.models import Credential
from devices.models import Device, ConnectionProtocol, Inventory, DeviceType



NEWLINE = str("\n")

# Create your views here.


class AutoSetDocstrings():
    """
    Utility class to auto-create Docstring from doctring of the view PLUS the docstring of the model
    """
    _initialized = False

    def __init__(self, *args, **kwargs):
        # create the docstring
        self.set_docstring()
        # mark the class as initialized so we don't run set_docstring() again
        self.__class__._initialized = True
        super().__init__(*args, **kwargs)

    def set_docstring(self):
        if not self._initialized:
            # we only want to run this once, not on re-initializations
            if self.__doc__:
                # add view docstring plus model docstring
                new_doc = self.__doc__ + NEWLINE + self.Meta.model.__doc__
            else:
                # add only model docstring
                new_doc = self.Meta.model.__doc__

            setattr(self.__class__, '__doc__', new_doc)

    class Meta:
        abstract = True


# ViewSets define the view behavior.


class CredentialViewSet(AutoSetDocstrings, viewsets.ModelViewSet):
    """
    Use this to create a new tunnel request
    """
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer

    class Meta:
        model = Credential


class DeviceViewSet(AutoSetDocstrings, viewsets.ModelViewSet):
    """
    [API usage directions]
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    class Meta:
        model = Device


class TemplateViewSet(AutoSetDocstrings, viewsets.ModelViewSet):
    """
    [API usage directions]
    """
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

    class Meta:
        model = Template


class TemplateGroupViewSet(AutoSetDocstrings, viewsets.ModelViewSet):
    """
    [API usage directions]
    """
    queryset = TemplateGroup.objects.all()
    serializer_class = TemplateGroupSerializer

    class Meta:
        model = TemplateGroup


class ConnectionProtocolViewSet(AutoSetDocstrings, viewsets.ModelViewSet):
    """
    [API usage directions]
    """
    queryset = ConnectionProtocol.objects.all()
    serializer_class = ConnectionProtocolSerializer

    class Meta:
        model = ConnectionProtocol


class InventoryViewSet(AutoSetDocstrings, viewsets.ModelViewSet):
    """
    [API usage directions]
    """
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    class Meta:
        model = Inventory


class DeviceTypeViewSet(AutoSetDocstrings, viewsets.ModelViewSet):
    """
    [API usage directions]
    """
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer

    class Meta:
        model = DeviceType
