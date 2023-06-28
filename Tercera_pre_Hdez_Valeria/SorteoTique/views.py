from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from SorteoTique.models import *

# Create your views here.

def inicio(request):
    return render(request, "SorteoTique/inicio.html")

def draws(request):
    return render(request, "SorteoTique/draws.html")

def clients(request):
    return HttpResponse("Vista client")

def sellers(request):
    return HttpResponse("Vista seller")

def prizes(request):
    return HttpResponse("Vista prize")

def tickets(request):
    return HttpResponse("Vista ticket")

