from django.shortcuts import render
from .models import User
from django.http import JsonResponse

# Create your views here.

def login_view(request):
    if request.session.get("username"):
        return JsonResponse({"message": "You are already logged in",
                             "username": request.session.get("username")
                            })
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check if user exists and password is correct
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                # Create a session for the user
                request.session.set_expiry(20)
                request.session["username"] = username
                return JsonResponse({"message": "Login successful", "status": 200})
            else:
                return JsonResponse({"message": "Incorrect password", "status": 401})
        except User.DoesNotExist:
            return JsonResponse({"message": "User not found", "status": 404})
        except Exception as e:
            return JsonResponse({"message": str(e), "status": 500})
    
    return render(request, "session_app/login.html")