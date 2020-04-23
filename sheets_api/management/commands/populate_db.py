from django.utils import timezone
from sheets_api.utils import (
    get_sheets_data,
    parse_month_and_day,
    parse_hour,
    get_last_index
)
from django.core.management.base import BaseCommand
from main.models import Event, Category
# import sys
from dateutil.parser import parse
from app_user.models import AppUser


class Command(BaseCommand):

    def _create_events(self):
        # sys.path.append('/home/kenan/django/event_project/')
        user = AppUser.objects.get(email="test@g.co")
        category = Category.objects.get(id=1)
        values = get_sheets_data()
        index = get_last_index()
        for row in range(index-1):
            if values[row][0] is not None and values[row][0] is not '':
                data = parse_month_and_day(values[row][0])
            if values[row][4] is not None and values[row][4] is not '':
                hour_minute = parse_hour(values[row][4])
            hour = int(hour_minute[0])
            minute = int(hour_minute[1])

            print(type(hour))
            print(type(minute))
            Event.objects.create(
                author=user,
                title=values[row][3],
                event_url=values[row][5],
                venue=values[row][2],
                community=values[row][1],
                desc=values[row][3],
                category=category,
                featured=True,
                date=parse(f'2020-{data[0]}-{data[1]} {hour}:{minute}')
                # date=timezone.datetime(
                #     year=2020,
                #     month=data[0],
                #     day=data[1],
                #     hour=hour,
                #     minute=25
                # )
            )

    def handle(self, *args, **options):
        self._create_events()
