from django.db import models
# Second Git practice change
# Create your models here.
class Parking(models.Model):
    STATUS_CHOICES = [
        ('Parked', 'Parked'),
        ('Free', 'Free'),
    ]
    vehicle_type=models.CharField(max_length=25)
    vehicle_number = models.CharField(max_length=25)
    owner_name = models.CharField(max_length=50)
    parked_hours = models.IntegerField()
    paid_amount = models.IntegerField()
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='Free')

    def __str__(self):
        return self.vehicle_number
