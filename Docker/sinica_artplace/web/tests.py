from django.test import TestCase
from django.urls import reverse

from .views import IndexView


class WebIndexTestCase(TestCase):
    def test_form(self):
        response = self.client.get(reverse('web:index'))
        self.assertIn('form', response.context)