from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from SorteoTique.models import *

# Create your views here.

def inicio(request):
    return render(request,"SorteoTique/inicio.html")

def test(request):
    prueba = Client.objects.all()
    return render(request, "SorteoTique/client.html",{"prueba": prueba})
    