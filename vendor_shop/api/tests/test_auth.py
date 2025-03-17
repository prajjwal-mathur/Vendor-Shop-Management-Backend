from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status


class VendorAuthTests(APITestCase):
    def test_register_vendor(self):
        """Test vendor registration"""
        data = {"username": "vendor1", "password": "testpass123", "full_name": "Vendor One"}
        response = self.client.post("/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_login_vendor(self):
        """Test vendor login and token retrieval"""
        user = User.objects.create_user(username="vendor1", password="testpass123")
        data = {"username": "vendor1", "password": "testpass123"}
        response = self.client.post("/login/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
