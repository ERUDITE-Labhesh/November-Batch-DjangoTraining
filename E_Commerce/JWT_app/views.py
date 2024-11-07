from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken

from django.contrib.auth import authenticate,login
# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
    
        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            refresh_token=RefreshToken.for_user(user)
            access_token=AccessToken.for_user(user)
            return JsonResponse({
                "access_token": str(access_token),
                "refresh_token": str(refresh_token)
            })

    return render(request, "JWT_app/login.html")