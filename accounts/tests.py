from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

# Create your tests here.
class CustomUserTests(TestCase):
    """A class that tests user model"""
    def test_create_user(self):
        """Tests creation of a regular user"""
        User = get_user_model()
        user = User.objects.create_user(
                username='abby',
                email='abbycherono@gmail.com',
                password='Testpass123'
                )
        self.assertEqual(user.username, 'abby')
        self.assertEqual(user.email, 'abbycherono@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """Tests creation of an admin user"""
        User = get_user_model()
        user = User.objects.create_superuser(
                username='Steve',
                email='steveomo95@gmail.com',
                password='Testpass123'
                )
        self.assertEqual(user.username, 'Steve')
        self.assertEqual(user.email, 'steveomo95@gmail.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class SignUpTests(TestCase):
    username = 'newuser'
    email = 'newuser@gmail.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, 'I should not be on this page'
            )

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
                self.username, self.email
                )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
                [0].email, self.email)
