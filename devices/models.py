from django.db import models

# Create your models here.


class Device(models.Model):
    seed_host_or_ip = models.TextField()
    hostname = models.TextField(blank=True)
    vendor = models.TextField(blank=True)
    model = models.TextField(blank=True)
    software = models.TextField(blank=True)
    device_type = models.TextField(blank=True)

    def __str__(self):
        return self.seed_host_or_ip

