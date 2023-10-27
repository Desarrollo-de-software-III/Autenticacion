# authentication/tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

class SignupTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_user_data = {
            "email": "test@example.com",
            "password": "testpassword",
            "username": "testuser"
        }

    def test_valid_signup(self):
        response = self.client.post(reverse('signup'), self.valid_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('token' in response.data)

    def test_invalid_email(self):
        invalid_data = self.valid_user_data.copy()
        invalid_data['email'] = 'invalid_email'
        response = self.client.post(reverse('signup'), invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_duplicate_email(self):
        User.objects.create_user(**self.valid_user_data)
        response = self.client.post(reverse('signup'), self.valid_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
