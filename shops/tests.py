from django.test import TestCase
from shops.utils import haversine
from rest_framework.test import APIClient
from shops.models import Shop

class HaversineTestCase(TestCase):
    def test_same_location(self):
        """Test the distance between identical points should be 0."""
        lat, lon = 40.730610, -73.935242
        distance = haversine(lat, lon, lat, lon)
        self.assertEqual(distance, 0.0)

    def test_known_distance(self):
        """Test the distance between known locations."""
        # distance between New York City (40.730610, -73.935242) and Los Angeles (34.052235, -118.243683)
        lat1, lon1 = 40.730610, -73.935242  # New York City
        lat2, lon2 = 34.052235, -118.243683  # Los Angeles
        distance = haversine(lat1, lon1, lat2, lon2)
        expected_distance = 3936  # Approximate distance in km
        self.assertAlmostEqual(distance, expected_distance, delta=5)

    def test_another_distance(self):
        """Test the distance between two other cities."""
        # Distance between Paris (48.8566, 2.3522) and Berlin (52.5200, 13.4050)
        lat1, lon1 = 48.8566, 2.3522  # Paris
        lat2, lon2 = 52.5200, 13.4050  # Berlin
        distance = haversine(lat1, lon1, lat2, lon2)
        expected_distance = 878  # Approximate distance in km
        self.assertAlmostEqual(distance, expected_distance, delta=5)
        
class ShopSearchAPITestCase(TestCase):
        def setUp(self):
            """Set up some test data."""
            # Create some shops for testing
            Shop.objects.create(name="New York Shop", latitude=40.730610, longitude=-73.935242)  # New York City
            Shop.objects.create(name="Los Angeles Shop", latitude=34.052235, longitude=-118.243683)  # Los Angeles
            Shop.objects.create(name="Paris Shop", latitude=48.8566, longitude=2.3522)  # Paris

        def test_search_nearby_shops(self):
            """Test searching for nearby shops and ensuring distance is calculated correctly."""
            client = APIClient()

            # Perform a search near New York City
            response = client.get('/shops/api/search/', {'latitude': 40.730610, 'longitude': -73.935242})

            # Assert the response is 200 OK
            self.assertEqual(response.status_code, 200)

            # Extract the response data
            data = response.json()

            # There should be 3 shops in the response
            self.assertEqual(len(data), 3)

            # The first shop should be the New York Shop with a distance of 0
            self.assertEqual(data[0]['shop']['name'], 'New York Shop')
            self.assertEqual(data[0]['distance'], 0.0)

        def test_search_far_location(self):
            """Test searching from a far location (Los Angeles)."""
            client = APIClient()

            # Perform a search near Los Angeles
            response = client.get('/shops/api/search/', {'latitude': 34.052235, 'longitude': -118.243683})

            # Assert the response is 200 OK
            self.assertEqual(response.status_code, 200)

            # Extract the response data
            data = response.json()

            # The first shop should be the Los Angeles Shop with a distance of 0
            self.assertEqual(data[0]['shop']['name'], 'Los Angeles Shop')
            self.assertEqual(data[0]['distance'], 0.0)

            # The second shop should be New York Shop, but at a distance of approximately 3936 km
            self.assertEqual(data[1]['shop']['name'], 'New York Shop')
            self.assertAlmostEqual(data[1]['distance'], 3936, delta=5)
