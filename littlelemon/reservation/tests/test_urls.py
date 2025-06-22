from django.test import SimpleTestCase
from django.urls import reverse, resolve
from reservation.views import get_bookings, create_booking, booking_detail, get_menus, create_menu, menu_detail
## PLEASE: Read the README FILE for guidance. Thank you.
class TestUrls(SimpleTestCase):
    # Booking
    def test_get_bookings_resolves(self):
        url = reverse('get_bookings')
        self.assertEqual(resolve(url).func, get_bookings)
    
    def test_create_booking_resolves(self):
        url = reverse('create_booking')
        self.assertEqual(resolve(url).func, create_booking)
    
    def test_booking_detail_resolves(self):
        url = reverse('booking_detail', args=[1])
        self.assertEqual(resolve(url).func, booking_detail)
    
    # Menu
    def test_get_menus_resolves(self):
        url = reverse('get_menus')
        self.assertEqual(resolve(url).func, get_menus)
    
    def test_create_menu_resolves(self):
        url = reverse('create_menu')
        self.assertEqual(resolve(url).func, create_menu)
    
    def test_menu_detail_resolves(self):
        url = reverse('menu_detail', args=[1])
        self.assertEqual(resolve(url).func, menu_detail)