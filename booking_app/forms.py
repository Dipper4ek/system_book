from django import forms
from .models import Car, Customer, Rental
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'year', 'price_per_day', 'horsepower', 'is_available', 'image']

class EmailLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            self.user = authenticate(email=email, password=password)
            if self.user is None:
                raise forms.ValidationError("Невірний email або пароль")
        return cleaned_data

    def get_user(self):
        return self.user
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['full_name', 'email', 'phone_number', 'password']

class RentalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['car'].queryset = Car.objects.filter(is_available=True)

    start_date = forms.DateField(
        input_formats=['%d.%m.%Y'],
        widget=forms.DateInput(format='%d.%m.%Y', attrs={'placeholder': 'дд.мм.рррр'})
    )
    end_date = forms.DateField(
        input_formats=['%d.%m.%Y'],
        widget=forms.DateInput(format='%d.%m.%Y', attrs={'placeholder': 'дд.мм.рррр'})
    )

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