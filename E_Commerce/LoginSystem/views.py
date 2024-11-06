from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from LoginSystem.models import LoginSystem
from LoginSystem.serializers import LoginSystemSerializer

from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def Homepage(request): 
    return render(request, 'LoginSystem/homepage.html')

def Indexpage(request): 
    return render(request, 'LoginSystem/indexpage.html')


'''
CRUD Operations 
C --> Create --> POST() 
R --> Read --> GET() 
U --> Update --> PUT() 
D --> Delete --> DELETE()
'''

# function based views 
@csrf_exempt
def AllUserData(request):
    try:
        all_users_data = LoginSystem.objects.all()
    except: 
        data = {
            "message":'Not Found Sorry!',
            "status": 404
        }
        return JsonResponse(data)
    
    if request.method == 'GET': # Reading 
        user_all_data_s = LoginSystemSerializer (all_users_data, many = True)
        return JsonResponse(user_all_data_s.data, safe=False)
    
    elif request.method == 'POST': # Addusers
        input_data = JSONParser().parse(request)
        user_data_s = LoginSystemSerializer(data = input_data)

        if user_data_s.is_valid():
            user_data_s.save()
            return JsonResponse(user_data_s.data, status = 201)
        else:
            return JsonResponse(user_data_s.error, status = 400)

@csrf_exempt
def SingleUserData(request, pk):
    try:
        user_data = LoginSystem.objects.get(pk=pk)
    except:
        data = {
            "message":'User Not Found Sorry!',
            "status": 404
        }
        return JsonResponse(data, status = 404)
    
    if request.method == 'GET':
        user_data_s = LoginSystemSerializer (user_data)
        return JsonResponse(user_data_s.data, safe=False)
    
    elif request.method == 'PUT':
        input_data = JSONParser().parse(request)
        user_data_s = LoginSystemSerializer(user_data, data = input_data)

        if user_data_s.is_valid():
            user_data_s.save()
            return JsonResponse(user_data_s.data, status = 202)
        else:
            return JsonResponse(user_data_s.error, status = 400)
        
    elif request.method == 'DELETE': 
        user_data.delete()
        data = {
             "message":'Successfully deleted',
            "status": 204
        }
        return JsonResponse(data, status = 204)
        

        
        





