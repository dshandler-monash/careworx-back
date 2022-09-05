import json
from django.shortcuts import render
from django.forms.models import model_to_dict
#from django.http import JsonResponse

#django rest framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

#import serializer
from services.serializers import ServiceSerializer

from services.models import Service
# Create your views here.

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    Careworx API View
    """
    instance = Service.objects.all().order_by("?").first() #serializer
    data = {}
    if model_data:
        data = ProductSerializer(instance).data

    return JsonResponse(data)

#def api_home(request, *args, **kwargs):
    # Generate JsonResponse from request
    #model_data = Service.objects.all().order_by("?").first()
    #data = {}
    #if model_data:
    #    data = model_to_dict(model_data)
    #body = request.body
    #data = {}
    #try:
    #    data = json.loads(body) # takes string of json -> python dict
    #except:
    #    pass
    #data['params'] = dict(request.GET) #request.GET gets URL query params
    #data['headers'] = dict(request.headers)
    #data['content_type'] = request.content.type
    
    #return JsonResponse(data)
