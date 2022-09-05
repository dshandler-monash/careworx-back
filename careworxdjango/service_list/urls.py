from django.urls import path
from . import views

urlpatterns = [
   path('servicelist/', views.service_list),
]