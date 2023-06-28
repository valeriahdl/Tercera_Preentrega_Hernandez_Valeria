from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from SorteoTique.models import Client
from SorteoTique.forms import formRegisterClient

# Create your views here.

def inicio(request):
    return render(request, "SorteoTique/inicio.html")

def draws(request):
    return render(request, "SorteoTique/draws.html")

def clients(request):
    Clients = Client.objects.all()
    return render(request, "SorteoTique/clients.html",{"Clients":Clients})

def sellers(request):
    return render(request, "SorteoTique/sellers.html")

def prizes(request):
    return render(request, "SorteoTique/prizes.html")

def tickets(request):
    #return HttpResponse("Vista ticket")
    return render(request, "SorteoTique/tickets.html")

def registerClient(request):
    Clients = Client.objects.all()
    if request.method == 'POST':
        client = Client(client_id=request.POST["client_id"], name=request.POST["name"],last_name=request.POST["last_name"],email=request.POST["email"])
        client.save()   
            #para que el formulario se limpie despues de meterlo:
        myForm = formRegisterClient()
        return render(request, "SorteoTique/registerClient.html", {"myForm":myForm, "Clients":Clients})
    else:
        myForm = formRegisterClient()
    return render(request, "SorteoTique/registerClient.html", {"myForm":myForm, "Clients":Clients})


