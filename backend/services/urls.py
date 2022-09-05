from django.urls import path

from . import views

urlpatterns = [
    path('',views.ServiceListCreateAPIView.as_view()),
    path('<int:pk>/',views.ServiceDetailAPIView.as_view())
]