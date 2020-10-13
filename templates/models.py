from django.db import models

# Create your models here.


class Templates(models.Model):
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(blank=True)

    def __str__(self):
        return self.name


class TemplateGroups(models.Model):
    group = models.CharField(max_length=100)
    deleted = models.BooleanField(blank=True)

    def __str__(self):
        return self.name