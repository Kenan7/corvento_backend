from django.core.management.base import BaseCommand
from main.models import Event, Category
from app_user.models import AppUser
from django.utils import timezone


class Command(BaseCommand):

    def _create_events(self):
        user = AppUser.objects.get(email="test@g.co")
        category = Category.objects.get(id=1)
        date = timezone.now()
        for i in range(500):
            Event.objects.create(
                author=user,
                title=f"Event Title --- {i}",
                event_url="http://www.corvento.com/",
                venue="Corvento.com/",
                community="DSC",
                description="""
                Test description ashjasdasjb dasd basjbk djasdbjasbdkjabjsdkbajskd
                """,
                category=category,
                featured=True,
                date=date,
                image="event_images/11NISANMeetUP_DSFzUxY.jpg"
            )

    def handle(self, *args, **options):
        self._create_events()
