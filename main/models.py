from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Event(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=1024)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image = VersatileImageField(
        upload_to="event_images", blank=True
    )
    venue = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
