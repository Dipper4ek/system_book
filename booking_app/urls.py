from django.urls import path
from .views import add_car, register_customer, Available_cars, create_rental
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.urls import path
from booking_app import views
from .views import email_login_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',  Available_cars.as_view(template_name='available_cars.html'), name='home'),
    path('available-cars/', Available_cars.as_view(template_name='available_cars.html'), name='available_cars'),
    path('add-car/', add_car, name='add_car'),
    path('register-customer/', register_customer, name='register_customer'),
    path('car-success/', TemplateView.as_view(template_name='car_success.html'), name='car_success'),
    path('customer-success/', TemplateView.as_view(template_name='customer_success.html'), name='customer_success'),
    path('rent-car/', create_rental, name='rent_car'),
    path('login/', email_login_view, name='login'),
    path('login-success/', TemplateView.as_view(template_name='login_success.html'), name='login_success'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
