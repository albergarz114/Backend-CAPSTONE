from django.db import models

## PLEASE: Read the README FILE for guidance. Thank you.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    numberofguests = models.IntegerField()
    bookingdate = models.DateField()

    def __str__(self):
        return self.name

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.title