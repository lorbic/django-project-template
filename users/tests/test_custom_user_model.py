from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserModelTests(TestCase):
    """Test that the user is successfully created"""

    def get_sample_user(self, email='test@lrbc.ml'):
        User = get_user_model()
        return User.objects.create_user(
            email=email,
            password='P@ssw0rd#123'
        )
    
    def get_sample_superuser(self, email='test_admin_user@lrbc.ml',):
        User = get_user_model()
        return User.objects.create_superuser(
            email=email,
            password='P@ssw0rd#123'
        )
    
    def test_create_user(self):
        """Test that the regular user is successfully created with
            correct parameters and permissions."""

        user = self.get_sample_user()

        self.assertEqual(user.email, 'test@lrbc.ml')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """Test that superuser is created succeddfully"""
        superuser = self.get_sample_superuser()

        self.assertEqual(superuser.email, 'test_admin_user@lrbc.ml')
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_email_is_not_verified_for_new_users(self):
        """Test that by default new users have unverified email status"""
        user = self.get_sample_user()
        self.assertFalse(user.is_email_verified)

        superuser = self.get_sample_superuser()
        self.assertFalse(superuser.is_email_verified)

    def test_email_address_is_unique(self):
        """Test that two users cannot use same email address"""
        User = get_user_model()

        user1 = self.get_sample_user(email='testuser@lrbc.ml')

        users = User.objects.filter(email=user1.email)

        self.assertEqual(len(users), 1)

