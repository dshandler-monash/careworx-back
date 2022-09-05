from django.urls import path
from . import views

urlpatterns = [
   path('service_list/', views.service_list),
]