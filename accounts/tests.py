from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username="test", email="test@tests.com", password="testpass123")
        self.assertEqual(user.username, "test")
        self.assertEqual(user.email, "test@tests.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(username="test", email="test@tests.com", password="testpass123")
        self.assertEqual(user.username, "test")
        self.assertEqual(user.email, "test@tests.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
