from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Service
from .serializers import ServiceSerializer
#from backend.services import serializers

class ServiceCreateAPIView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer  

# class ServiceDetailAPIView(generics.RetrieveAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
    
    #first lookup_field = 'pk'

    #lookup_field = 'suburb'


    #def get_queryset():
      
# class ServiceListAPIView(generics.ListAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer

class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):

    queryset = Service.objects.all() #queryset
    serializer_class = ServiceSerializer
    lookup_field = 'pk' # change here for retrieveModelMixin

    def get(self, request, *args, **kargs):
        pk = kargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kargs)
        return self.list(request, *args, **kargs)

@api_view(['GET'])
def product_alt_view(request, pk=None, *args, **kargs):
    method = request.method

    if method == "GET":
        #detail view
        if pk is not None:
            #detail view
            obj = get_object_or_404(Service, pk=pk) # gives object or http404
            data = ServiceSerializer(obj, many=False).data
            return Response(data)
        #list view
        qs = Service.objects.all() #queryset
        data = ServiceSerializer(qs, many=True).data
        return Response(data)