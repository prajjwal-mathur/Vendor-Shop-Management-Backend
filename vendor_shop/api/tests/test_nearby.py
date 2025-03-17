from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Shop

class NearbyShopsTests(APITestCase):
    def setUp(self):
        """Create a test vendor and some shops"""
        self.user = User.objects.create_user(username="vendor1", password="testpass123")
        Shop.objects.create(name="Shop A", owner=self.user, type_of_business="Grocery", latitude=37.77, longitude=-122.41)
        Shop.objects.create(name="Shop B", owner=self.user, type_of_business="Electronics", latitude=37.78, longitude=-122.42)

    def test_nearby_shops(self):
        """Test fetching nearby shops within radius"""
        response = self.client.get("/shops/nearby/?lat=37.7749&lon=-122.4194&radius=5")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)  # At least one shop should be nearby
