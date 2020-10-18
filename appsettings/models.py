from django.db import models

# Create your models here.


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
