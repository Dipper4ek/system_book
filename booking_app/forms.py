from django import forms
from .models import Car, Customer, Rental

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'year', 'price_per_day', 'horsepower', 'is_available', 'image']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['full_name', 'email', 'phone_number']

class RentalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Фільтруємо поле car, щоб показати тільки доступні машини
        self.fields['car'].queryset = Car.objects.filter(is_available=True)

    class Meta:
        model = Rental
        fields = ['car', 'customer', 'start_date', 'end_date']

    def clean(self):
        cleaned_data = super().clean()
        car = cleaned_data.get('car')
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if car and start_date and end_date:
            if not Rental.is_car_available(car, start_date, end_date):
                raise forms.ValidationError("Ця машина вже заброньована на вибраний період.")
        return cleaned_data