from django.db import models

# Create your models here.


class Device(models.Model):
    seed_host_or_ip = models.CharField(max_length=100)
    hostname = models.CharField(max_length=100, blank=True)
    vendor = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100, blank=True)
    software = models.CharField(max_length=100, blank=True)
    device_type = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.seed_host_or_ip

