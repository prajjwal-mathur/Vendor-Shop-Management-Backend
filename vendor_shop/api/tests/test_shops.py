from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Shop

class ShopTests(APITestCase):
    def setUp(self):
        """Create a test vendor and authenticate"""
        self.user = User.objects.create_user(username="vendor1", password="testpass123")
        self.client.force_authenticate(user=self.user)  # Authenticate for all tests

    def test_create_shop(self):
        """Test shop creation"""
        data = {"name": "Shop A", "type_of_business": "Grocery", "latitude": 12.34, "longitude": 56.78}
        response = self.client.post("/shops/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Shop.objects.count(), 1)

    def test_read_shops(self):
        """Test fetching shop list"""
        Shop.objects.create(name="Shop A", owner=self.user, type_of_business="Grocery", latitude=12.34, longitude=56.78)
        response = self.client.get("/shops/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_shop(self):
        """Test shop update"""
        shop = Shop.objects.create(name="Old Shop", owner=self.user, type_of_business="Clothing", latitude=10.0, longitude=20.0)
        response = self.client.put(f"/shops/{shop.id}/", {"name": "Updated Shop", "type_of_business": "Clothing", "latitude": 10.0, "longitude": 20.0})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        shop.refresh_from_db()
        self.assertEqual(shop.name, "Updated Shop")

    def test_delete_shop(self):
        """Test deleting a shop"""
        shop = Shop.objects.create(name="Shop A", owner=self.user, type_of_business="Grocery", latitude=12.34, longitude=56.78)
        response = self.client.delete(f"/shops/{shop.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Shop.objects.count(), 0)
