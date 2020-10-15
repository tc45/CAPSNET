from rest_framework import serializers
# from django.contrib.auth.models import User
from apptemplates.models import Template, TemplateGroup
from appsettings.models import Credential
from devices.models import Device, ConnectionProtocol, Inventory, DeviceType


# Serializers define the API representation.


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'  # we can override this dynamically


class CredentialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Credential
        fields = '__all__'  # we can override this dynamically


class TemplateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'  # we can override this dynamically


class TemplateGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TemplateGroup
        fields = '__all__'  # we can override this dynamically


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'  # we can override this dynamically


class ConnectionProtocolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConnectionProtocol
        fields = '__all__'  # we can override this dynamically


class InventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'  # we can override this dynamically


class DeviceTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeviceType
        fields = '__all__'  # we can override this dynamically