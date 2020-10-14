from django.db import models
from devices.models import Device

# Create your models here.


class TemplateGroup(models.Model):
    group = models.CharField(max_length=100, help_text="Group name")
    description = models.CharField(max_length=100, blank=True, help_text="Description")
    deleted = models.BooleanField(blank=True)

    def __str__(self):
        return self.group


class Template(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True)
    group = models.ForeignKey(TemplateGroup, blank=False, null=False, on_delete=models.PROTECT, help_text="Template Group", verbose_name="Template Group")
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(blank=True)

    def __str__(self):
        return self.name




