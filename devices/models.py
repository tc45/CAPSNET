from django.db import models
from django.utils import timezone


# Abstract base classes
class TrackedModel(models.Model):
    """
    Adds basic items change tracking
    """
    created = models.DateTimeField(editable=False, blank=True, null=True, help_text="When created")
    changed = models.DateTimeField(editable=False, blank=True, null=True, help_text="Last changed")

    def pre_save(self):
        if self.changed is None:  # first time new object only
            self.created = timezone.now()
        self.changed = timezone.now()  # update every save/update

    def save(self, *args, **kwargs):
        self.pre_save()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True  # does not inherit

# Create your models here.


class DeviceType(models.Model):
    type_name = models.CharField(max_length=256, unique=True, blank=False, null=False, help_text="Device type (unique)")
    description = models.CharField(max_length=64, default="", blank=True, null=True, help_text="Short description")

    def __str__(self):
        out_str = str(self.type_name)
        if self.description not in ["", " ", None]:
            out_str += " (" + str(self.description) + ")"
        return out_str


class ConnectionProtocol(models.Model):
    protocol_name = models.CharField(max_length=256, unique=True, blank=False, null=False, help_text="Device type (unique)")
    protocol_port = models.IntegerField(default=0, blank=False, null=False, help_text="TCP/UDP port")
    description = models.CharField(max_length=64, default="", blank=True, null=True, help_text="Short description")

    def __str__(self):
        return str(self.protocol_name) + " (port: " + str(self.protocol_port) + ")"


class Credential(models.Model):
    username = models.CharField(max_length=256, blank=False, null=False, help_text="Login username")
    password = models.CharField(max_length=256, blank=True, null=True, help_text="Login password")
    enable_pass = models.CharField(max_length=256, blank=True, null=True, help_text="Enable password (if needed)")
    description = models.CharField(max_length=64, default="", blank=True, null=True, help_text="Short description")

    def __str__(self):
        out_str = str(self.username)
        if self.description not in ["", " ", None]:
            out_str += " (" + str(self.description) + ")"
        return out_str

    def stored_password(self):
        """
        Only added this to have a "redacted field" to display in admin forms/lists
        This implies that the saved password exists, when the change form shows blank fields
        """
        return "********"


class Device(TrackedModel):
    enable = models.BooleanField(default=True, help_text="Enable/Disable scanning of this device")
    management_ip = models.GenericIPAddressField(unique=True, default=None, max_length=15, blank=False, null=False, help_text="Management IP")
    hostname = models.CharField(default=None, max_length=256, blank=True, null=True, help_text="Device HOSTNAME")
    vendor = models.CharField(max_length=100, blank=True, help_text="Device vendor name")
    model = models.CharField(max_length=100, blank=True, help_text="Device model name")
    software = models.CharField(max_length=100, blank=True, help_text="Device software version")
    device_type = models.CharField(max_length=100, blank=True, help_text="Device softare filename")
    connection_protocol = models.ForeignKey(ConnectionProtocol, on_delete=models.PROTECT, blank=True, default=None, help_text="Choose connection protocol/port")
    credential = models.ForeignKey(Credential, on_delete=models.PROTECT, blank=True,default=None,
                                            help_text="Choose authentication username")
    device_type = models.ForeignKey(DeviceType, blank=True, on_delete=models.PROTECT)
    notes = models.TextField(default=None, blank=True, null=True, help_text="Notes")

    def __str__(self):
        device_name = ""
        if self.hostname:
            device_name = self.hostname
            if self.management_ip:
                device_name += " (" + str(self.management_ip) + ")"
        elif self.management_ip:
            device_name = self.management_ip

        return device_name

    def common_name(self):
        return self.__str__()

    def save(self, *args, **kwargs):
        if self.changed is None:  # first time new object only
            self.created = timezone.now()
        self.changed = timezone.now()  # update every save/update
        super().save(*args, **kwargs)


class Inventory(models.Model):
    device = models.ForeignKey(Device, related_name="inventory_task", blank=False, null=False, on_delete=models.CASCADE,
                               help_text="Device")
    part_id = models.CharField(max_length=100, help_text="Part number", blank=True)
    notes = models.CharField(max_length=100, default=None, blank=True, null=True, help_text="Notes")

    def __str__(self):
        device_name = ""
        if self.device.hostname:
            device_name = self.device.hostname
            if self.device.management_ip:
                device_name += " - " + str(self.device.management_ip)
        elif self.device.management_ip:
            device_name = self.device.management_ip

        return self.part_id + " (" + device_name + ")"

