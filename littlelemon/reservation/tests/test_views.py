from django.test import TestCase, Client
from django.urls import reverse
from reservation.models import Booking, Menu
from reservation.serializers import BookingSerializer, MenuSerializer
import json
from datetime import date
from rest_framework import status
from rest_framework.test import APIClient
## PLEASE: Read the README FILE for guidance. Thank you.
class TestViews(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.booking = Booking.objects.create(
            name = "Test User",
            numberofguests = 4,
            bookingdate = date(2025, 12, 23)
        )

        self.menu = Menu.objects.create(
            title = "Test Title",
            price = 23.99,
            inventory = 50
        )

        #URLS
        self.booking_list_url = reverse('get_bookings')
        self.booking_create_url = reverse('create_booking')
        self.booking_detail_url = reverse('booking_detail', args=[self.booking.pk])

        self.menu_list_url = reverse('get_menus')
        self.menu_create_url = reverse('create_menu')
        self.menu_detail_url = reverse('menu_detail', args=[self.menu.pk])

    # Helper method to create test data
    def get_valid_booking_data(self):
        return {
            'name' : "Test User",
            'numberofguests' : 4,
            'bookingdate' : '2025-12-23'
        }
        
    def get_valid_menu_data(self):
        return {
            'title' : "Test Title",
            'price' : 23.99,
            'inventory' : 50
        }
        
    ## BOOKING TESTS
    def test_booking_list_GET(self):
        response = self.client.get(self.booking_list_url)   
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1) 

    def test_booking_create_POST_valid(self):
        response = self.client.post(
        self.booking_create_url,
        data=self.get_valid_booking_data(),  # No need for json.dumps
        format='json'  # Let DRF handle serialization
    )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], "Test User")
        self.assertEqual(response.data['numberofguests'], 4)
    
    def test_booking_create_POST_invalid(self):
        invalid_data = {
            'numberofguests': 25
        }

        response = self.client.post(
            self.booking_create_url,
            data=json.dumps(invalid_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
    
    def test_booking_detail_GET(self):
        response = self.client.get(self.booking_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], self.booking.name)
    
    def test_user_detail_PUT_valid(self):
        data = self.get_valid_booking_data()
        response = self.client.put(
            self.booking_detail_url,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.name, 'Test User')
    
    def test_booking_detail_DELETE(self):
        response = self.client.delete(self.booking_detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Booking.objects.count(), 0)

    ## MENU UNIT TESTING
    def test_menu_list_GET(self):
        response = self.client.get(self.menu_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_menu_create_POST_valid(self):
        data = self.get_valid_menu_data()
        response = self.client.post(
            self.menu_create_url,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Menu.objects.count(), 2) 
    

    def test_menu_create_POST_invalid(self):
        invalid_data = {
            'price': 100
        }

        response = self.client.post(
            self.menu_create_url,
            data=json.dumps(invalid_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_menu_detail_GET(self):
        response = self.client.get(self.menu_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], self.menu.title)
    

    def test_menu_detail_PUT_valid(self):
        data = self.get_valid_menu_data()
        response = self.client.put(
            self.menu_detail_url,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.menu.refresh_from_db()
        self.assertEqual(self.menu.title, 'Test Title')

    def test_menu_detail_DELETE(self):
        response = self.client.delete(self.menu_detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Menu.objects.count(), 0)