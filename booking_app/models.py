from django.db import models
from django.db.models import Q

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    horsepower = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.full_name} ({self.email})"


class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer.full_name} renting {self.car} from {self.start_date} to {self.end_date}"

    @staticmethod
    def is_car_available(car, start_date, end_date):
        # Перевіряємо, чи є бронювання машини з перетином дат
        conflicts = Rental.objects.filter(
            car=car,
            is_approved=True,
            start_date__lte=end_date,
            end_date__gte=start_date,
        )
        return not conflicts.exists()
