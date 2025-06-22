from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from .views import  index, get_bookings, create_booking, booking_detail, get_menus, create_menu, menu_detail
## PLEASE: Read the README FILE for guidance. Thank you.
urlpatterns = [
    
    path('bookings/', get_bookings, name='get_bookings'),
    path('bookings/create/', create_booking, name='create_booking'),
    path('bookings/<int:pk>/', booking_detail, name='booking_detail'),
    path('menus/', get_menus, name='get_menus'),
    path('menus/create/', create_menu, name='create_menu'),
    path('menus/<int:pk>/', menu_detail, name='menu_detail'),
    path('api-token-auth/', obtain_auth_token),
]