from versatileimagefield.fields import VersatileImageField
from django.db import models
# apps
from main.utils import TimeStampedModel
from fcm_django.models import FCMDevice
from django.db.models.signals import post_save, post_delete
from time import sleep
from django.db.models import Q


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

    fcm_device = models.OneToOneField(
        FCMDevice,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    REQUIRED_FIELDS = []

    def __str__(self):
        # return f"{self.email} - {self.firebase_id}"
        return self.email


def connect_app_user_to_fcm_device(sender, instance, created, **kwargs):
    if created:
        print("Signal received. I will try to create fcm device now...")
        temp_fcm_device = FCMDevice.objects.create(
            name=instance.email,
            device_id=instance.firebase_id,
            registration_id=instance.firebase_token,
            active=True,  # True for now -- There will be a settings for this.
            type=u"android",
        )
        print("I created the device", temp_fcm_device,
              "I will try to connect that device to our user now...")
        instance.fcm_device = temp_fcm_device
        instance.save()
        print("yess, I did it!", instance.fcm_device)


def delete_fcm_device_object(sender, instance, **kwargs):
    try:
        temp_dev = FCMDevice.objects.get(
            Q(name=instance.email) | Q(device_id=instance.firebase_id)
        )
        temp_dev.delete()
    except:
        print("there is not connected device")


class ContactForm(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=1024)

    def __str__(self):
        return f"{self.email} --- {self.subject}"


post_save.connect(connect_app_user_to_fcm_device, sender=AppUser)
post_delete.connect(delete_fcm_device_object, sender=AppUser)
