from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Homepage(request): 
    return render(request, 'LoginSystem/homepage.html')

def Indexpage(request): 
    return render(request, 'LoginSystem/indexpage.html')

