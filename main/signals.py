from django.conf import settings
from main.utils import unique_slug_generator, TimeStampedModel
from django.db.models.signals import pre_save, post_save
from app_user.models import AppUser
from google.cloud import firestore
from django.utils import timezone
import os
import logging

logger = logging.getLogger(__name__)


def event_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(
            instance, instance.title)


def category_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(
            instance, instance.name)


def event_send_notification_post_save(sender, instance, created, update_fields, *args, **kwargs):
    if instance.published:
        instance.send_notification()


def enter_notification_to_firestore(title):
    try:
        path = "/home/kenan/evento.json"
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path
        now = timezone.now()
        list = AppUser.ojects.all()

        data = {
            "title": "Yeni Etkinlik var",
            "data": title,
            "date": now,
            "isRead": 0,
        }
    except:
        logger.error('error with google-creds - path - time - appuser object')

    try:
        db = firestore.Client()

        for i in range(len(list)):
            user = list[i]
            try:
                doc_ref = db.collection(u'users')\
                    .document(user.firebase_id)\
                    .collection(u'notifications')\
                    .add(data)
                print(doc_ref)
            except:
                print(f'Error for ---- {user} ----')
    except IndexError:
        logger.error('Something with the list index')
    except:
        logger.error(
            'Could not establish connection or send data to firestore')
