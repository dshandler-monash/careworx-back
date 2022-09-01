from curses.ascii import HT
from django.shortcuts import render, HttpResponse

# Create your views here.

def Index(request):
    return HttpResponse("It is working!")