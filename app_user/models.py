from versatileimagefield.fields import VersatileImageField
from django.db import models
# apps
from main.utils import TimeStampedModel
from fcm_django.models import FCMDevice
from django.db.models.signals import post_save, post_delete
from time import sleep
from django.db.models import Q
import logging

logger = logging.getLogger(__name__)


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
        try:
            logger.debug(
                'Signal received. I am trying to create FCMDevice object for your AppUser account...')
            temp_fcm_device = FCMDevice.objects.create(
                name=instance.email,
                device_id=instance.firebase_id,
                registration_id=instance.firebase_token,
                # True for now -- There will be a settings for this.
                active=True,
                type=u"android",
            )
            logger.debug(
                'I created the device - %s - I will try to connect that device to our user now...', temp_fcm_device)
            instance.fcm_device = temp_fcm_device
            instance.save()
            logger.debug('Instance saved')
        except:
            logger.error('Could not create FCMDevice object for user!')


def delete_fcm_device_object(sender, instance, **kwargs):
    try:
        temp_dev = FCMDevice.objects.get(
            Q(name=instance.email) | Q(device_id=instance.firebase_id)
        )
        temp_dev.delete()
        logger.debug('Found and deleted -- %s', temp_dev)
    except:
        logger.debug('there is not connected device')


class ContactForm(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=1024)

    def __str__(self):
        return f"{self.email} --- {self.subject}"


post_save.connect(connect_app_user_to_fcm_device, sender=AppUser)
post_delete.connect(delete_fcm_device_object, sender=AppUser)
