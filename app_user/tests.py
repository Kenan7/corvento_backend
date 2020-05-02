from django.test import TestCase
from app_user.models import AppUser


class UserCreateTest(TestCase):

    def test_create_user(self):
        user = AppUser.objects.create(
            email='test@user.com',  slug="usr"
        )
        self.assertEqual(user.email, 'normal@user.com')
        self.assertEqual(user.slug, "usr")
