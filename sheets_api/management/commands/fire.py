from django.core.management.base import BaseCommand
from google.cloud import firestore
from app_user.models import AppUser
from django.utils import timezone


class Command(BaseCommand):

    def _tts(self):

        db = firestore.Client()

        list = AppUser.objects.all()

        user = AppUser.objects.all().first()
        now = timezone.now()

        data = {
            "title": "instance.title",
            "data": "instance.title",
            "date": now,
            "isRead": 0,
        }

        for i in range(len(list)):
            user = list[i]
            try:
                doc_ref = db.collection(u'users')\
                    .document(user.firebase_id)\
                    .collection(u'notifications')\
                    .add(data)
                list.pop(i)
            except:
                print(f'Error for ---- {user} ----')

    def handle(self, *args, **options):
        self._tts()
