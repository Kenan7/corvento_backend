from django.contrib.auth.models import User, AbstractUser, UserManager
from versatileimagefield.fields import VersatileImageField
from django.db import models
import uuid as uuid_lib
# apps
from main.utils import TimeStampedModel


class AppUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('gender', 2)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class AppUser(AbstractUser, TimeStampedModel):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('NON', 'Prefer Not to Say')
    )

    slug = models.SlugField(unique=True, blank=True, null=True)

    uuid = models.UUIDField(
        primary_key=True,
        default=uuid_lib.uuid4,
        editable=False)

    email = models.EmailField(('email address'), unique=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=4)
    image = VersatileImageField(
        upload_to="user_images", blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = AppUserManager()

    def __str__(self):
        return f"{self.email} - {self.get_full_name()}"

    def get_short_name(self):
        return self.first_name
