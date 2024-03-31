from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserRegistrationAndLoginTests(APITestCase):
    def setUp(self):
        self.registration_url = reverse('user-registration')
        self.login_url = reverse('login')

    def test_registration(self):
        """
        Teste die Benutzerregistrierung.
        """
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword123',
            'password2': 'testpassword123'
        }
        response = self.client.post(self.registration_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='testuser').exists())
        user = User.objects.get(username='testuser')
        self.assertTrue(Token.objects.filter(user=user).exists())

    def test_login(self):
        """
        Teste das Login und ob ein Token zurückgegeben wird.
        """
        self.test_registration()
        login_data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
        response = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Create your tests here.
