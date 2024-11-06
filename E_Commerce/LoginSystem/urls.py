from . import views
from django.urls import path

urlpatterns = [
    path('', views.Homepage),
    path('indexpage/', views.Indexpage),
    path('allusersdata/', views.AllUserData),
    path('user-data/<int:pk>/', views.SingleUserData),
]