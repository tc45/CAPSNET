from django.contrib import admin
from .models import Device, Credential, ConnectionProtocol, DeviceType, Inventory

admin.site.register(Device)
admin.site.register(Credential)
admin.site.register(ConnectionProtocol)
admin.site.register(DeviceType)
admin.site.register(Inventory)