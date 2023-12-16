from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.shortcuts import render
from rest_framework import permissions, filters
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from cars.serializers import CarSerializer, OwnerSerializer
from cars.models import Car, Owner
from django_filters.rest_framework import DjangoFilterBackend


class CarAPIView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['id', 'car_brand', 'registration_number', 'car_owner', 'year_of_manufacture', 'car_colour', 'registration_date' ]
    search_fields = ['id', 'car_brand', 'registration_number', 'car_owner', 'car_colour']
    ordering_fields = ['id', 'car_brand', 'registration_number', 'car_owner', 'year_of_manufacture', 'car_colour', 'registration_date' ]
