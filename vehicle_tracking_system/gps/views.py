from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json
import serial
from .models import Vehicle, GPSData

@csrf_exempt
def gps_data(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        gps_data = json.loads(data)
        vehicle = Vehicle.objects.get(license_plate=gps_data['vehicle'])
        timestamp = datetime.strptime(gps_data['timestamp'], '%H:%M:%S').time()
        location = GPSData.objects.create(
            vehicle=vehicle,
            timestamp=timestamp,
            location=gis_models.Point(float(gps_data['longitude']), float(gps_data['latitude']))
        )
        return HttpResponse('OK')
    else:
        return HttpResponse('Invalid request method')
