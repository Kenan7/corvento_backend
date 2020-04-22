from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.conf import settings
from main.utils import unique_slug_generator, TimeStampedModel
from django.db.models.signals import pre_save

User = settings.AUTH_USER_MODEL


class EventManager(models.Manager):
    def get_featured(self):
        return super(EventManager, self).get_queryset().filter(featured=1)


class Event(TimeStampedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=1024)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image = VersatileImageField(
        upload_to="event_images", blank=True
    )
    venue = models.CharField(max_length=120)
    date = models.DateTimeField()
    event_url = models.URLField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    featured = models.BooleanField()
    community = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    objects = EventManager()

    ordering = ['date']

    def __str__(self):
        return f"{self.author.first_name} - {self.title}"


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=64)
    icon = models.CharField(max_length=64, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name


def event_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(
            instance, instance.title)


def category_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(
            instance, instance.name)


pre_save.connect(event_slug_pre_save_receiver, sender=Event)
pre_save.connect(category_slug_pre_save_receiver, sender=Category)
