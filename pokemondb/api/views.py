from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def pokemon_type(request):
    data = {"results": "hello"}
    return JsonResponse(data)
    