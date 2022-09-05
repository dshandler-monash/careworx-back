from curses.ascii import HT
from django.shortcuts import render
from django.http import JsonResponse
from .models import ServiceList
from .serializers import ServiceListSerializers
# Create your views here.

def service_list(request):
    # Get all services, serialize them and return json

    services = ServiceList.objects.all()
    serializer = ServiceListSerializers(services, many=True)
    return JsonResponse(serializer.data, safe=False)