from django.test import TestCase
from django.urls import reverse

class FortunaISKTest(TestCase):
    def test_main_view(self):
        response = self.client.get(reverse('fortunaisk:main_view'))
        self.assertEqual(response.status_code, 200)
