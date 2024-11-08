from django.contrib import admin
from django.urls import path, include

from .views import divide_by_zero

urlpatterns = [
  path('div-check/',divide_by_zero),
]
