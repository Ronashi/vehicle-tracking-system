from django.urls import path
from . import views

urlpatterns = [
    path('gps_data/', views.gps_data, name='gps_data'),
]
