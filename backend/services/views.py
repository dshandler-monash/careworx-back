from rest_framework import generics

from .models import Service
from .serializers import ServiceSerializer

class ServiceDetailAPIView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
    #first lookup_field = 'pk'

    #lookup_field = 'suburb'


    #def get_queryset():