from django.urls import path
from . import views

urlpatterns = [
	path('rental', views.all_rentals, name='all_rentals'),
	path('rental/<int:rental_id>', views.rental, name='rental'),
	path('rental/add', views.add_rental, name='add_rental'),
	path('vehicle', views.all_vehicles, name='all_vehicles'),
	path('vehicle/<int:vehicle_id>', views.vehicle, name='vehicle'),
	path('vehicle/add', views.add_vehicle, name='add_vehicle'),
	path('customer', views.all_customers, name='all_customers'),
	path('customer/<int:customer_id>', views.customer, name='customer'),
	path('customer/add', views.add_customer, name='add_customer'),
	path('station', views.all_stations, name='all_stations'),
	path('station/<int:station_id>', views.station, name='station'),
	path('station/add', views.add_station, name='add_station'),
]
