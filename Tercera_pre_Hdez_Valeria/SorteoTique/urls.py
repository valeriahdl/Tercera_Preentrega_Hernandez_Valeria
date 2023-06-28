from django.urls import path
from SorteoTique.views import *

urlpatterns = [

    path('inicio/', inicio, name ="Inicio"),
    path('draws/', draws, name="Draws"),
    path('clients/', clients, name="Clients"),
    path('sellers/', sellers, name="Sellers"),
    path('prizes/', prizes, name="Prizes"),
    path('tickets/', tickets, name="Tickets"),
    
   
]
