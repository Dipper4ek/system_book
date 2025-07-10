"""
URL configuration for booking_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path
from booking_app.views import add_car, Available_cars, home_page, car_success, customer_success, register_customer, create_rental

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page, name='home'),
    path('', home_page, name='home'),
    path('available-cars/', Available_cars.as_view(), name='available_cars'),
    path('add-car/', add_car, name='add_car'),
    path('register-customer/', register_customer, name='register_customer'),
    path('car-success/', car_success, name='car_success'),
    path('customer-success/', customer_success, name='customer_success'),
    path('rent-car/', create_rental, name='rent_car'),
]



