from django.utils.text import slugify
import string
import random
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# slug generator
DONT_USE = ['create']


def random_string_generator(
        size=2, chars=string.ascii_lowercase + string.digits
):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, value, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(value)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = f"{slug}-{random_string_generator(size=4)}"
        return unique_slug_generator(instance, value, new_slug=new_slug)
    return slug
