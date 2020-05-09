from versatileimagefield.fields import VersatileImageField
from django.db import models
# apps
from main.utils import TimeStampedModel
from fcm_django.models import FCMDevice
from django.db.models.signals import post_save
from time import sleep


class AppUser(TimeStampedModel):
    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True
    )

    firebase_id = models.CharField(
        max_length=400,
        null=True,
        blank=True
    )

    email = models.EmailField(
        ('email address'),
        unique=True
    )

    image = VersatileImageField(
        upload_to="user_images",
        blank=True
    )

    firebase_token = models.CharField(
        max_length=400,
        null=True,
        blank=True
    )

    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} - {self.firebase_id}"


def connect_app_user_to_fcm_device(sender, instance, **kwargs):
    sleep(5)
    FCMDevice.objects.create(
        name=instance.email,
        device_id=instance.firebase_id,
        registration_id=instance.firebase_token,
        active=True,  # True for now -- There will be a settings for this.
        type=u"android",
    )


post_save.connect(connect_app_user_to_fcm_device, sender=AppUser)


class ContactForm(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=1024)

    def __str__(self):
        return f"{self.email} --- {self.subject}"
