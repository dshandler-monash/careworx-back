import json
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def api_home(request, *args, **kwargs):
    # Generate JsonResponse from request
    
    body = request.body
    data = {}
    try:
        data = json.loads(body) # takes string of json -> python dict
    except:
        pass
    data['params'] = dict(request.GET) #request.GET gets URL query params
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content.type
    
    return JsonResponse(data)
