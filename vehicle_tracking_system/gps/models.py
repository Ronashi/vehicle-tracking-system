from django.db import models
from django.contrib.gis.db import models as gis_models
from datetime import datetime

class Vehicle(models.Model):
    license_plate = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

class GPSData(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    timestamp = models.TimeField()
    location = gis_models.PointField()
