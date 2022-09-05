from django.db import models
from django.db.models import Q
# Create your models here.

class ServiceQuerySet(models.QuerySet):
    
    def search(self, query):
        return self.filter(suburb__icontains.query)

class ServiceManager(models.Manager):

    def search(self, query):
        lookup = Q(suburb__icontains=query) | Q(post_code__icontains=query)
        return Service.objects.filter(lookup)

class Service(models.Model):
    ## Model for ServiceListDB attained from python manage.py inspectdb
    service_name = models.CharField(max_length=255, blank=True, null=True)
    address_1 = models.CharField(max_length=255, blank=True, null=True)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    suburb = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    post_code = models.CharField(max_length=255, blank=True, null=True)
    planning_region_2019 = models.CharField(max_length=255, blank=True, null=True)
    care_type = models.CharField(max_length=255, blank=True, null=True)
    residential_places = models.IntegerField(blank=True, null=True)
    home_places = models.IntegerField(blank=True, null=True)
    restorative_places = models.IntegerField(blank=True, null=True)
    provider_name = models.CharField(max_length=255, blank=True, null=True)
    org_type = models.CharField(max_length=255, blank=True, null=True)
    abs_remoteness = models.CharField(max_length=255, blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    lon = models.CharField(max_length=255, blank=True, null=True)
    federal_funding_2021 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_list'
