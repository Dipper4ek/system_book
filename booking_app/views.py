from django.views.generic import ListView
from .models import Car
from django.shortcuts import render, redirect
from .forms import CarForm, CustomerForm, RentalForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import EmailLoginForm
from django.contrib import messages
from .models import Customer


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

class Available_cars(ListView):
    model = Car
    template_name = 'available_cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return Car.objects.filter(is_available=True)


@login_required
def create_rental(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            rental = form.save(commit=False)
            rental.is_approved = True  # чи False, залежно від логіки
            rental.save()

            # Оновлюємо статус машини
            rental.car.is_available = False
            rental.car.save()

    else:
        form = RentalForm()

    return render(request, 'rental_form.html', {'form': form})



def email_login_view(request):
    if request.method == 'POST':
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('login_success')
    else:
        form = EmailLoginForm()
    return render(request, 'auth/customer_login.html', {'form': form})




def customer_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            customer = Customer.objects.get(email=email)
            if customer.password == password:
                request.session['customer_id'] = customer.id  # Зберігаємо сесію
                return redirect('home')  # або інша сторінка
            else:
                messages.error(request, 'Невірний пароль')
        except Customer.DoesNotExist:
            messages.error(request, 'Користувача з таким email не знайдено')

    return render(request, 'auth/customer_login.html')

def profile_view(request):
    if 'customer_id' not in request.session:
        return redirect('login')
    ...

def customer_logout(request):
    request.session.flush()
    return redirect('login')
