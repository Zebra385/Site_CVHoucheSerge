from django.test import TestCase
from django.urls import reverse
from .views import AccueilView

class AccueilPageTestCase(TestCase):
    """
    Test that accueil page returns a 200 if the item exists.
    """
    def test_accueil_page(self):
        response = self.client.get(reverse('cv:accueil'))
        self.assertEqual(response.status_code, 200)