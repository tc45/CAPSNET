from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Abstract base classes
class TrackedModel(models.Model):
    """
    Adds basic items change tracking
    """
    created = models.DateTimeField(editable=False, blank=True, null=True, help_text="When created")
    changed = models.DateTimeField(editable=True, blank=True, null=True, help_text="Last changed")

    def pre_save(self):
        if self.changed is None:  # first time new object only
            self.created = timezone.now()
        self.changed = timezone.now()  # update every save/update

    def save(self, *args, **kwargs):
        self.pre_save()
        super().save(*args, **kwargs)
        return self

    class Meta:
        abstract = True  # does not inherit


class Credential(TrackedModel):
    username = models.CharField(max_length=256, blank=False, null=False, help_text="Login username")
    password = models.CharField(max_length=256, blank=True, null=True, help_text="Login password")
    enable_pass = models.CharField(max_length=256, blank=True, null=True, help_text="Enable password (if needed)")
    description = models.CharField(max_length=64, default="", blank=True, null=True, help_text="Short description")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

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


class CustomerGeneral(TrackedModel):
    CustomerName = models.CharField(max_length=256, unique=True, blank=False, null=False, help_text="Customer Name")
    CustomerDescription = models.CharField(max_length=256, unique=False, blank=True, null=True, help_text="Customer Description")
    primaryContactFirstName = models.CharField(max_length=256, unique=False, blank=True, null=True, help_text="Customer First Name")
    primaryContactLastName = models.CharField(max_length=256, unique=False, blank=True, null=True, help_text="Customer Last Name")
    primaryContactEmail = models.EmailField(max_length=256, unique=False, blank=True, null=True, help_text="Contact Email")
    primaryContactCellPhone = models.CharField(max_length=256, unique=False, blank=True, null=True, help_text="Contact Cell Phone")
    primaryContactWorkPhone = models.CharField(max_length=256, unique=False, blank=True, null=True, help_text="Contact Work Phone")
    primaryContactAddress1 = models.CharField(max_length=256, unique=False, blank=True, null=True, help_text="Contact Address")
    primaryContactAddress2 = models.CharField(max_length=256, unique=False, blank=True, null=True, help_text="Contact Address2")
    primaryContactCity = models.CharField(max_length=256, unique=False, blank=True, null=True, help_text="Contact City")

    def __str__(self):
        return str(self.CustomerName)


