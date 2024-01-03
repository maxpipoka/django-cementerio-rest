from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import Taxpayer

class TaxpayerTests(APITestCase):

    def setUp(self):
        self.url = reverse('taxpayer-list')
        self.data = {
            'code': 12, 
            'name': 'Mart', 
            'dni': 29285854, 
            'address':'La casa de Martin',
            'city_address':'El pueblo donde vive martin'}
        self.taxpayer = Taxpayer.objects.create(**self.data)

    
    def test_taxpayer_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_OK_200)

        