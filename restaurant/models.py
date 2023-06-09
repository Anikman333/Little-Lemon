from django.db import models

# Create your models here.

class Booking(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveIntegerField()
    booking_date = models.DateField()

    def __str__(self):
        return self.name
    
class Menu(models.Model):
    ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.PositiveIntegerField()

    def __str__(self):
        return self.title   