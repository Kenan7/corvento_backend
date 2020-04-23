from django.test import TestCase
from django.contrib.auth import get_user_model


class UserCreateTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='normal@user.com', password='kkk', username='testusername', first_name="user",  slug="usr"
        )
        self.assertEqual(user.email, 'normal@user.com')
        self.assertEqual(user.username, 'testusername')
        self.assertEqual(user.first_name, "user")
        self.assertEqual(user.slug, "usr")
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
