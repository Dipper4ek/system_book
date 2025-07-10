from django.contrib import admin
from .models import Car, Customer, Rental

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('customer', 'car', 'start_date', 'end_date', 'is_approved')
    list_filter = ('is_approved', 'start_date')
    search_fields = ('customer__full_name', 'car__brand', 'car__model')
    list_editable = ('is_approved',)
admin.site.register(Car)
admin.site.register(Customer)

