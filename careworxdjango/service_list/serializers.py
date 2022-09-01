from rest_framework import serializers
from .models import ServiceList


class ServiceListSerializers(serializers.ModelSerializers):
    class Meta:
        model = ServiceList
        fields = '__all__'

    