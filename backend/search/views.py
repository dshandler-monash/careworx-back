from rest_framework import generics

from services.models import Service
from services.serializers import ServiceSerializer

class SearchListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self, *args, **kargs):
        qs = super().get_queryset(*args, **kargs) 
        q = self.request.GET.get('q')
        results = qs.search(q)
        return results
