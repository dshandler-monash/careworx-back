from rest_framework import generics

from services.models import Service
from services.serializers import ServiceSerializer

from django.shortcuts import get_object_or_404

class SearchListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self, *args, **kargs):
        qs = super().get_queryset(*args, **kargs) 
        q = self.request.GET.get('q')
        #results = Service.objects.none()
        #if q is not None:
        results = qs.search(q)
        return results
#obj = get_object_or_404(Service, pk=pk)