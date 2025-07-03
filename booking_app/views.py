from django.views.generic import ListView
from .models import Car
from django.shortcuts import render, redirect
from .forms import CarForm, CustomerForm

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car_success')
    else:
        form = CarForm()
    return render(request, 'add_car.html', {'form': form})

def car_success(request):
    return render(request, 'car_success.html')
def home_page(request):
    return render(request, 'home.html')
def customer_success(request):
    return render(request, 'customer_success.html')
def register_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_success')
    else:
        form = CustomerForm()
    return render(request, 'register_customer.html', {'form': form})

class available_cars(ListView):
    model = Car
    template_name = 'available_cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return Car.objects.filter(is_available=True)
