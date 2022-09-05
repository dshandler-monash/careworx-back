from curses.ascii import HT
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'service_list/index.html')