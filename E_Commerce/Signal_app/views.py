from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def divide_by_zero(request):
    result=10/5
    return JsonResponse({
        "result": result,
    })