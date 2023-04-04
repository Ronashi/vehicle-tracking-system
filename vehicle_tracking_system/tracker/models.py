from django.db import models

# Create your models here.
from django.db import models
from django.contrib.gis.db import models as gis_models

class Vehicle(models.Model):
    name = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=10)

class GPSData(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    location = gis_models.PointField()
