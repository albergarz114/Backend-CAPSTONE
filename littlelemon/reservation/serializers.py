from rest_framework import serializers
from .models import Booking, Menu

## PLEASE: Read the README FILE for guidance. Thank you.

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'name', 'numberofguests', 'bookingdate']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']