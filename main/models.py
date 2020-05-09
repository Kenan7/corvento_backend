from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.conf import settings
from main.utils import TimeStampedModel
from django.db.models.signals import pre_save, post_save
from app_user.models import AppUser
from fcm_django.models import FCMDevice
from tinymce import HTMLField
from google.cloud import firestore
from django.utils import timezone
from main.signals import (
    event_slug_pre_save_receiver,
    event_send_notification_post_save,
    category_slug_pre_save_receiver,
    enter_notification_to_firestore
)
import logging

logger = logging.getLogger(__name__)


class EventManager(models.Manager):
    def get_featured(self):
        return super(EventManager, self).get_queryset().filter(featured=1)


class Event(TimeStampedModel):
    author = models.ForeignKey(
        AppUser,
        on_delete=models.SET_NULL,
        null=True
    )

    title = models.CharField(max_length=128)

    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True
    )

    image = VersatileImageField(
        upload_to="event_images",
        blank=True
    )

    venue = models.CharField(max_length=120)

    date = models.DateTimeField()

    event_url = models.URLField(max_length=200)

    slug = models.SlugField(unique=True, blank=True)

    featured = models.BooleanField()

    community = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    description = HTMLField(
        'description',
        blank=True,
        null=True
    )

    published = models.BooleanField(
        default=False,
        verbose_name="""
        Etkinliği paylaş ve BİLDİRİM gönder""",
        help_text="""
        Bu özellik varsayılan olarak
        devre dışı olarak geliyor,
        aktifleştirildiğinde,
        etkinlik herkese görünür olur
        ve bu bilgilerle kullanıcılara
        bildirim gider
        """
    )

    objects = EventManager()

    ordering = ['date']

    def __str__(self):
        # return f"{self.author.email} - {self.title}"
        return self.title

    def send_notification(self):
        try:
            devices = FCMDevice.objects.all()
            try:
                devices.send_message(
                    title="Yeni etkinlik var",
                    body=self.title
                )
            except:
                logger.error('Could not send notification...')
            logger.debug(
                f"Success! Notification for this Event[{self.title} - {self.description}] has been sent!")
        except:
            logger.error('There is no FCM device...')

        enter_notification_to_firestore(self.title)


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=64)
    icon = models.CharField(max_length=64, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name


post_save.connect(event_send_notification_post_save, sender=Event)
pre_save.connect(event_slug_pre_save_receiver, sender=Event)
pre_save.connect(category_slug_pre_save_receiver, sender=Category)
