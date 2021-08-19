from django.db import models
from django.forms import ModelForm

# Create your models here.
class Address(models.Model):
	address = models.CharField(max_length=100)
	address2 = models.CharField(max_length=100, null=True)
	city = models.CharField(max_length=20)
	country = models.CharField(max_length=20)
	postal_code = models.IntegerField()

	def __str__(self):
		return f'{self.address}, {self.city}, {self.country}, {self.postal_code}'

class Customer(models.Model):
	first_name = models.CharField(max_length=20) 
	last_name = models.CharField(max_length=20)
	email = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=25)
	address = models.ForeignKey(Address, on_delete=models.CASCADE)

class Vehicle_Type(models.Model):
	name = models.CharField(max_length=200)

class Vehicle_Size(models.Model):
	name = models.CharField(max_length=200)

class Vehicle(models.Model):
	vehicle_type = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
	date_created =  models.DateTimeField()
	real_cost = models.IntegerField()
	size = models.ForeignKey(Vehicle_Size, on_delete=models.CASCADE)

	def is_rented(self):
		rentals = self.rental_set.filter(return_date__isnull=True)
		if len(rentals) > 0:
			return True
		return False 

class Rental(models.Model):
	rental_date = models.DateTimeField()
	return_date = models.DateTimeField(null=True)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class Rental_Rate(models.Model):
	daily_rate = models.IntegerField()
	vehicle_type = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
	vehicle_size = models.ForeignKey(Vehicle_Size, on_delete=models.CASCADE)

class Rental_Station(models.Model):
	name = models.CharField(max_length=20)
	capacity = models.IntegerField()
	address = models.ForeignKey(Address, on_delete=models.CASCADE)

class Rental_StationForm(ModelForm):
	class Meta:
		model = Rental_Station
		fields = ['name','capacity','address']

class VehicleAtRentalStation(models.Model):
	arrival_date = models.DateTimeField()
	departure_date = models.DateTimeField(null=True)
	vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
	rental_station = models.ForeignKey(Rental_Station, on_delete=models.CASCADE)
