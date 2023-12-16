# Generated by Django 4.0 on 2021-12-15 11:04

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('phone_number', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('email_address', models.EmailField(max_length=30)),
                ('tin_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=15)),
                ('car_brand', models.CharField(choices=[('toyota', 'TOYOTA'), ('nissan', 'NISSAN'), ('volkswagen', 'VOLKSWAGEN'), ('honda', 'HONDA'), ('BMW', 'BMW'), ('mercedes', 'MERCEDES')], default='toyota', max_length=20)),
                ('year of namufacture', models.DateField(max_length=15)),
                ('country_of_manufacture', models.CharField(max_length=20)),
                ('engine_capacity', models.CharField(max_length=20)),
                ('car_type', models.CharField(choices=[('saloon', 'SALOON'), ('lorry', 'LORRY'), ('truck', 'TRUCK')], default='saloon', max_length=20)),
                ('registration_date', models.DateField(max_length=15)),
                ('car_colour', models.CharField(choices=[('red', 'RED'), ('white', 'WHITE'), ('black', 'BLACK')], default='red', max_length=15)),
                ('number_of_seats', models.IntegerField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('car_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carowner')),
            ],
        ),
    ]
