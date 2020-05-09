from django.core.management.base import BaseCommand
from main.models import Event, Category
from app_user.models import AppUser


class Command(BaseCommand):

    def _delete_events(self):
        user = AppUser.objects.get(email="test@g.co")
        event = Event.objects.filter(author=user)
        for i in range(500):
            event.delete()

    def handle(self, *args, **options):
        self._delete_events()
