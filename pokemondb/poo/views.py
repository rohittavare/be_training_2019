from django.shortcuts import render, redirect
from django.http import JsonResponse
from pokemon.models import Pokemon

def handler(request, pName):
    return Pokemon.objects.filter(name__exact=pName)
    #return JsonResponse(data)                        # return some json