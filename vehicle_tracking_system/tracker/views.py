from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Vehicle, GPSData

def vehicle_map(request, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
    latest_gps_data = GPSData.objects.filter(vehicle=vehicle).latest('timestamp')
    context = {
        'vehicle': vehicle,
        'location': latest_gps_data.location,
    }
    return render(request, 'vehicle_map.html', context)
