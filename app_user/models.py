from versatileimagefield.fields import VersatileImageField
from django.db import models
import uuid as uuid_lib
# apps
from main.utils import TimeStampedModel


class AppUser(TimeStampedModel):
    slug = models.SlugField(unique=True, blank=True, null=True)

    uuid = models.UUIDField(
        primary_key=True,
        default=uuid_lib.uuid4,
        editable=False
    )
    firebase_id = models.CharField(max_length=120)

    email = models.EmailField(('email address'), unique=True)
    image = VersatileImageField(
        upload_to="user_images", blank=True
    )

    notifications = models.ForeignKey(
        "UserNotifications", on_delete=models.CASCADE, null=True, blank=True
    )

    firebase_token = models.CharField(max_length=64, null=True, blank=True)

    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} - {self.uuid}"


class UserNotifications(models.Model):
    title = models.CharField(max_length=32)
    data = models.CharField(max_length=200)
    date = models.DateTimeField()
