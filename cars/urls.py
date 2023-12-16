from django.urls import path
from cars.views import *

urlpatterns = [
    path('', CarAPIView.as_view()),
]
