from django.urls import path
from SorteoTique.views import *

urlpatterns = [
    
    path('inicio/', inicio),
    path('draws/', draws),
    path('clients/', clients),
    path('sellers/', sellers),
    path('prizes/', prizes),
    path('tickets/', tickets),
    
   
]
