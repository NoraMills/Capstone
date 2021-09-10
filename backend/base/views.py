from django.shortcuts import render
from django.http import JsonResponse

# function based views


def getRoutes(request):
    return JsonResponse('Hello', safe=False)
