from django.test import TestCase
from django.urls import reverse

from .views import *


class ContactUsViewTestCase(TestCase):
    def test_contactus_return_error_when_no_fields_sent(self):
        client = self.client
        response = client.post('/contact_us/leave_request/', data={}, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.data)

    def test_contactus_return_201(self):
        response = self.client.post('/contact_us/leave_request/', data={"name": 'denis', 'phone_number': '89110185385'}, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertContains(response, 'Ваш запрос принят. Ожидайте звонка')