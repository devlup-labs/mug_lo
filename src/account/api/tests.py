from django.test import TestCase
from django.shortcuts import reverse
from rest_framework import status
from django.contrib.auth.models import User


class AuthenticationCheckAPIViewTest(TestCase):
    def test_unauthenticated_response(self):
        response = self.client.get(reverse('api:account:auth-check'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'message': 'Unauthorized'})

    def test_authenticated_response(self):
        user = User.objects.create_user(username='test', password='testpass')
        self.client.login(username=user.username, password='testpass')
        response = self.client.get(reverse('api:account:auth-check'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'message': 'Authorized'})
