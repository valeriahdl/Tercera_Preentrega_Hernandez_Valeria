from django.urls import path, include
from SorteoTique.views import *

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('prueba/',test, name="prueba"),
]