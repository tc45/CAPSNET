from django.contrib import admin
from .models import Device, Credential, ConnectionProtocol, DeviceType, Inventory, SeedDevice, NewObject


class InventoryInline(admin.TabularInline):
    model = Inventory


class DeviceAdmin(admin.ModelAdmin):
    model = Device
    inlines = [
        InventoryInline
    ]
    readonly_fields = [
        'common_name',
    ]
    list_display = ['common_name', 'management_ip', ]



admin.site.register(Device, DeviceAdmin)
#admin.site.register(Credential)
admin.site.register(ConnectionProtocol)
admin.site.register(DeviceType)
admin.site.register(Inventory)
admin.site.register(SeedDevice)
admin.site.register(NewObject)

