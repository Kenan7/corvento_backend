from django.test import TestCase
from django.shortcuts import reverse
from app_user.models import AppUser
from django.contrib.auth import get_user_model

# class AppUserAPITests(TestCase):

#     def setUp(self):
#         AppUser.objects.get_or_create()


class UserCreateTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='normal@user.com', password='kkk', username='testusername', gender=2, first_name="user", last_name="name", slug="usr"
        )
        self.assertEqual(user.email, 'normal@user.com')
        self.assertEqual(user.username, 'testusername')
        self.assertEqual(user.first_name, "user")
        self.assertEqual(user.last_name, "name")
        self.assertEqual(user.slug, "usr")
        self.assertEqual(user.gender, 2)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser('kenan',
                                                   'super@user.com', 'foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
