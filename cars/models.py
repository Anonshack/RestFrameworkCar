from django.db import models
from phone_field import PhoneField

CAR_BRAND_CHOICES = (
    ('toyota', 'TOYOTA'),
    ('nissan', 'NISSAN'),
    ('volkswagen', 'VOLKSWAGEN'),
    ('honda', 'HONDA'),
    ('BMW', 'BMW'),
    ('mercedes', 'MERCEDES'),
)

CAR_TYPE_CHOICES = (
    ('saloon', 'SALOON'),
    ('lorry', 'LORRY'),
    ('truck', 'TRUCK'),
)

CAR_COLOUR_CHOICES = (
    ('red', 'RED'),
    ('white', 'WHITE'),
    ('black', 'BLACK'),
)


class Owner(models.Model):
    name = models.CharField(max_length=15)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    email_address = models.EmailField(max_length=30)
    tin_number = models.CharField(max_length=20)
    address = models.CharField(max_length=20)

    def __str__(self):
        return f" Owner Names: {self.name} | Email Address: {self.email_address} | TIN Number: {self.tin_number}"


class Car(models.Model):
    registration_number = models.CharField(max_length=15)
    car_brand = models.CharField(max_length=20, choices=CAR_BRAND_CHOICES, default='toyota')
    year_of_manufacture = models.DateField(max_length=15)
    country_of_manufacture = models.CharField(max_length=20)
    engine_capacity = models.CharField(max_length=20)
    car_type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES, default='saloon')
    registration_date = models.DateField(max_length=15)
    car_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car_colour = models.CharField(max_length=15, choices=CAR_COLOUR_CHOICES, default='red')
    number_of_seats = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" Vehicle Registration Number: {self.registration_number} | {self.car_owner} | Vehicle Type: {self.car_type}"
