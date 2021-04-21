from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    response = {
        'data' : 'Hello World'
    }
    return JsonResponse(response)