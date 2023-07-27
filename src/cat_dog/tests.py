from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class TestCatDogHome(TestCase):
    def test_get(self):
        response = self.client.get(reverse("catdog"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="home_page.html")
