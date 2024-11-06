from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('file-form/',views.file_upload_form,name="file_upload_form")
]
