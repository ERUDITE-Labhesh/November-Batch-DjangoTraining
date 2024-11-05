from . import views
from django.urls import path

urlpatterns = [
    path('', views.Homepage),
    path('indexpage/', views.Indexpage),
]