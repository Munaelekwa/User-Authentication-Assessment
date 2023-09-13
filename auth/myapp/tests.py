from django.test import TestCase
from django.urls import reverse
from .models import CustomUser

class UserRegistrationTests(TestCase):
    def test_user_registration_valid_data(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'password1': 'securepassword',
            'password2': 'securepassword',
        }
        response = self.client.post(reverse('registration'), data)
        self.assertEqual(response.status_code, 302)  # Successful redirection
        self.assertTrue(CustomUser.objects.filter(email=data['email']).exists())  # User created

    def test_user_registration_invalid_data(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'invalid-email',  # Invalid email format
            'password1': 'securepassword',
            'password2': 'differentpassword',  # Passwords do not match
        }
        response = self.client.post(reverse('registration'), data)
        self.assertEqual(response.status_code, 200)  # Form errors, stays on the registration page
        self.assertFalse(CustomUser.objects.filter(email=data['email']).exists())  # User not created


class UserAuthenticationTests(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'testuser@example.com',
            'password': 'securepassword',
            'first_name': 'Test',
            'last_name': 'User',
        }
        self.user = CustomUser.objects.create_user(**self.user_data)

    def test_user_login_valid_credentials(self):
        response = self.client.post(reverse('user_login'), self.user_data)
        self.assertEqual(response.status_code, 302)  # Successful redirection
        self.assertTrue(self.client.session['_auth_user_id'])  # User is logged in

    def test_user_login_invalid_credentials(self):
        data = {
            'email': 'testuser@example.com',
            'password': 'wrongpassword',  # Incorrect password
        }
        response = self.client.post(reverse('user_login'), data)
        self.assertEqual(response.status_code, 200)  # Login page with error message
        self.assertFalse(self.client.session.get('_auth_user_id'))  # User is not logged in

    def test_user_logout(self):
        self.client.login(email=self.user_data['email'], password=self.user_data['password'])
        response = self.client.get(reverse('user_logout'))
        self.assertEqual(response.status_code, 302)  # Successful redirection
        self.assertFalse(self.client.session.get('_auth_user_id'))  # User is logged out


class AuthenticatedUserAccessTests(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'testuser@example.com',
            'password': 'securepassword',
            'first_name': 'Test',
            'last_name': 'User',
        }
        self.user = CustomUser.objects.create_user(**self.user_data)
        self.client.login(email=self.user_data['email'], password=self.user_data['password'])

    def test_authenticated_user_can_access_protected_view(self):
        response = self.client.get(reverse('hello_world'))
        self.assertEqual(response.status_code, 200)  # Access granted for authenticated user

    def test_unauthenticated_user_cannot_access_protected_view(self):
        self.client.logout()
        response = self.client.get(reverse('hello_world'))
        self.assertEqual(response.status_code, 302)  # Redirected to login page for unauthenticated user


class AuthenticationSystemEdgeCaseTests(TestCase):
    def test_user_login_nonexistent_user(self):
        data = {
            'email': 'nonexistent@example.com',  # Non-existent user
            'password': 'securepassword',
        }
        response = self.client.post(reverse('user_login'), data)
        self.assertEqual(response.status_code, 200)  # Login page with error message

    def test_user_login_incorrect_password(self):
        data = {
            'email': 'testuser@example.com',
            'password': 'wrongpassword',  # Incorrect password
        }
        response = self.client.post(reverse('user_login'), data)
        self.assertEqual(response.status_code, 200)  # Login page with error message


class SecurityVulnerabilityTests(TestCase):
    def test_csrf_attack(self):
        response = self.client.get(reverse('registration'))
        self.assertContains(response, 'csrfmiddlewaretoken')  # CSRF token present in the registration form






