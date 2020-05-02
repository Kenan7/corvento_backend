from versatileimagefield.fields import VersatileImageField
from django.db import models
# apps
from main.utils import TimeStampedModel


class AppUser(TimeStampedModel):
    slug = models.SlugField(unique=True, blank=True, null=True)

    firebase_id = models.CharField(
        max_length=400, null=True, blank=True
    )

    email = models.EmailField(('email address'), unique=True)
    image = VersatileImageField(
        upload_to="user_images", blank=True
    )

    notifications = models.ForeignKey(
        "UserNotifications", on_delete=models.CASCADE, null=True, blank=True
    )

    firebase_token = models.CharField(max_length=400, null=True, blank=True)

    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} - {self.firebase_id}"


class UserNotifications(models.Model):
    title = models.CharField(max_length=32)
    data = models.CharField(max_length=200)
    date = models.DateTimeField()


class ContactForm(models.Model):
    user_id = models.ForeignKey(
        AppUser, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=1024)
