from django.test import TestCase
from reservation.models import Booking, Menu
from datetime import date

## PLEASE: Read the README FILE for guidance. Thank you.

class BookingModelTest(TestCase):
    def setUp(self):
        self.booking = Booking.objects.create(name="John", numberofguests=6, bookingdate=date(2025, 12, 5))

    def test_booking_creation(self):
        self.assertEqual(self.booking.name, "John")
        self.assertEqual(self.booking.numberofguests, 6)
        self.assertEqual(self.booking.bookingdate, date(2025, 12, 5))

    def test_booking_str(self):
        self.assertEqual(str(self.booking), "John")


class MenuModelTest(TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(title="Salmon", price=12.50, inventory=32)

    def test_menu_creation(self):
        self.assertEqual(self.menu.title, "Salmon")
        self.assertEqual(self.menu.price, 12.50)
        self.assertEqual(self.menu.inventory, 32)
    
    def test_menu_str(self):
        self.assertEqual(str(self.menu), "Salmon")