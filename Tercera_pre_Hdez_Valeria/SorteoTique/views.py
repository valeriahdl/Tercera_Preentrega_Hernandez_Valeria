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
    return render(request, "SorteoTique/clients.html")

def sellers(request):
    return render(request, "SorteoTique/sellers.html")

def prizes(request):
    return render(request, "SorteoTique/prizes.html")

def tickets(request):
    #return HttpResponse("Vista ticket")
    return render(request, "SorteoTique/tickets.html")

