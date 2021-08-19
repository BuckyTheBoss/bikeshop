from faker import Faker
from rent.models import *
import random
from django.utils import timezone

fake = Faker()

def generate_first_name():
	return fake.first_name()

def generate_last_name():
	return fake.last_name()

def generate_email():
	return fake.ascii_safe_email()

def generate_number():
	return fake.phone_number()

def generate_address():
	return fake.street_address()

def generate_address2():
	return fake.secondary_address()

def generate_country():
	return fake.country()

def generate_city():
	return fake.city()

def generate_start_date():
	return fake.date_time_between(start_date="-3y", end_date="-30d", tzinfo=None)

def generate_end_date():
	end_date = [fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None), None]
	return random.choice(end_date)

def generate_zip():
	return fake.zipcode()

def pick_customer():
	customers = Customer.objects.all()
	return random.choice(customers)

def pick_vehicle():
	vehicles = Vehicle.objects.all()
	for vehicle in vehicles:
		if not vehicle.is_rented():
			return vehicle
	return None	

		


def generate_customers(number):
	for i in range(0,number):
		print(f'adding customer #{i}')
		first_name = generate_first_name()
		last_name = generate_last_name()
		email = generate_email()
		phone_number = generate_number()
		address = generate_address()
		city = generate_city()
		country = generate_country()
		customer = Customer(first_name=first_name,last_name=last_name,email=email,phone_number=phone_number,address=address,city=city,country=country)
		customer.save()

def generate_rentals(number):
	rented_list = Rental.objects.filter(return_date__isnull=True).values('vehicle_id')
	unrented_list = Vehicle.objects.exclude(pk__in=rented_list)
	for i in range(0,number):
		rental = Rental(rental_date=generate_start_date(),return_date=generate_end_date(),customer=pick_customer(),vehicle=random.choice(unrented_list) )
		rental.save()

def generate_vehicles(number):
	sizes= Vehicle_Size.objects.all()
	types= Vehicle_Type.objects.all()
	costs= [2000,3000,4000]
	for i in range(0,number):
		vehicle = Vehicle(vehicle_type=random.choice(types), date_created=timezone.now(), real_cost=random.choice(costs), size=random.choice(sizes))
		vehicle.save()

def fix_cust_addy():
	customers = Customer.objects.all()
	addresses = Address.objects.all()
	for customer in customers:
		customer.address = random.choice(addresses)
		customer.save()

def generate_addresses(number):
	for i in range(0,number):
		addy = Address(address=generate_address(), address2=generate_address2(), city=generate_city(), country=generate_country(), postal_code=generate_zip())
		addy.save()

def generate_station(number):
	addresses = Address.objects.all()
	for i in range(0, number):	
		address = random.choice(addresses)
		station = Rental_Station(name=address.address, capacity= random.randint(5,25), address=address)
		station.save()

def populate_stations():
	# every rental record should have a corresponding VehicleAtRentalStation record
	# the rental_date should be identical to the departure_date
	start_date = generate_start_date()
	for rental in Rental.objects.all():
		record = VehicleAtRentalStation(arrival_date=start_date,departure_date=rental.rental_date,vehicle=rental.vehicle,rental_station=random.choice(Rental_Station.objects.all()))
		record.save()
		if rental.return_date is not None:
			start_date = rental.return_date



