from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse("<br><br><h1>Hola,</h1> este es un test. Si estás aquí por favor escribe /SorteoTique/inicio en el buscador")

def deSorteo(self, aleatorio):
    data = f"Lo que quiera escribir en negritas: <h1>{aleatorio}</h1>"
    return HttpResponse(data)

def templateTest(self):
    nombre = "Valeria"
    apellido = "Hernandez"

    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
    }
    template1= loader.get_template("template.html")
    documento = template1.render(diccionario)
    return HttpResponse(documento)