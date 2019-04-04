from django.shortcuts import render, redirect
from .models import *
from django.utils import timezone

# Create your views here.
def all_rentals(request):
	rental_list = Rental.objects.all().order_by('return_date')
	print(rental_list)
	return render(request, 'all_rentals.html', {"rental_list" : rental_list})

def rental(request,rental_id):
	rental = Rental.objects.filter(id=rental_id).first()
	return render(request, 'rental.html', {'rental' : rental})

def add_rental(request):
	customers = Customer.objects.all()
	rented_list = Rental.objects.filter(return_date__isnull=True).values('vehicle_id')
	unrented_list = Vehicle.objects.exclude(pk__in=rented_list)
	
	if request.method == 'POST':
		cust_id = request.POST.get('customer_id')
		vehicle_id = request.POST.get('vehicle_id')
		vehicle = Vehicle.objects.filter(id=vehicle_id).first()
		customer = Customer.objects.filter(id=cust_id).first()
		vehicle_rentals = Rental.objects.filter(vehicle_id=vehicle_id, return_date__isnull=True).first()

		if customer is None: 
			#flash message with no cust found
			return render(request, 'add_rental.html',{'customers' : customers})

		elif vehicle is None:
			#flash message with no vehicle found
			return render(request, 'add_rental.html',{'customers' : customers})

		elif vehicle_rentals is not None:
			#flash message that vehicle is rented out
			return render(request, 'add_rental.html',{'customers' : customers})

		rental = Rental(rental_date=timezone.now(),customer=customer,vehicle=vehicle)
		rental.save()
		return redirect('all_rentals')
	return render(request, 'add_rental.html',{'customers' : customers, 'unrented_list' : unrented_list})

def all_vehicles(request):
	vehicle_list = Vehicle.objects.all()
	rented_list = Rental.objects.filter(return_date__isnull=True).values('vehicle_id')
	unrented_list = Vehicle.objects.exclude(pk__in=rented_list)
	return render(request, 'all_vehicles.html', {'vehicle_list' : vehicle_list, 'unrented_list' : unrented_list})

def vehicle(request,vehicle_id):
	vehicle = Vehicle.objects.filter(id=vehicle_id).first()
	return render(request, 'vehicle.html', {'vehicle' : vehicle})

def add_vehicle(request):
	types = Vehicle_Type.objects.all()
	sizes = Vehicle_Size.objects.all()
	if request.method == 'POST':
		vehicle_size = Vehicle_Size.objects.filter(id=request.POST.get('size')).first()
		vehicle_type = Vehicle_Type.objects.filter(id=request.POST.get('type')).first()
		vehicle = Vehicle(vehicle_type=vehicle_type, date_created=timezone.now(),real_cost=request.POST.get('real_cost'),size=vehicle_size)
		vehicle.save()
		return redirect('all_vehicles')
	return render(request, 'add_vehicle.html', {'types' : types, 'sizes' : sizes })


def add_customer(request):
	
	if request.method == 'POST':

		if Customer.objects.filter(email=request.POST.get('email')).first() != None:
			#flash message saying email in use
			return redirect('add_customer')

		customer = Customer(first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'),email=request.POST.get('email'),phone_number=request.POST.get('phone_number'),address=request.POST.get('address'),city=request.POST.get('city'),country=request.POST.get('country'))
		customer.save()
		return redirect('all_customers')
	return render(request, 'add_customer.html')

def all_customers(request):
	customer_list = Customer.objects.all()
	return render(request, 'all_customers.html', {'customer_list' : customer_list})

def customer(request, customer_id):
	customer = Customer.objects.filter(id=customer_id).first()
	return render(request, 'customer.html', {'customer' : customer} )
