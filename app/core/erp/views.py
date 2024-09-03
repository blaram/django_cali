from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def myfirstview(request):
    data = {
        'name': 'Blas'
    }
    return JsonResponse(data)