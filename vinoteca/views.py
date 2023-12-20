from django.shortcuts import render
import json
from django.http import HttpResponse
from django.shortcuts import render
from .models import Vino, Contacto
import pandas as pd

def contacto(request):
    form = Contacto()
    return render(request, "formulario.html", {'form': form})

def index(request):
    return render(request, "index.html")

def registro(request):
    return render(request, "registro.html")

def lista_vinos(request):
    #vinos = list(Vino.objects.values())
    vinos = Vino.objects.all()
    return render(request, "listado.html", {"vinos": vinos})

def buscar_vino(request):
    return render(request, "buscar_vino.html")

def ver_vino(request):
    busqueda = request.GET["vino"]
    vino = Vino.objects.get(id=busqueda)
    return render(request, "ver_vino.html", {"vino": vino})

def resultado(request):
    return render(request, "resultado.html")

def guardarExcel(request):
    ruta = 'vinoteca/static/Wines.xlsx' 
    df = pd.read_excel(ruta, index_col=0) #Leyendo el archivo excell como un dataframe
    df = df.sort_values(by=['Points'], ascending=False).head(999)
    json_records = df.reset_index().to_json(orient ='records')  
    vinos = json.loads(json_records)
        
    for vino in vinos:
        vinoDB = Vino(cosecha=vino["Vintage"],pais=vino["Country"],region=vino["County"],designacion=vino["Designation"],puntos=vino["Points"],precio=vino["Price"],provincia=vino["Province"],nombre=vino["Title"],cepas=vino["Variety"],bodega=vino["Winery"])
        vinoDB.save()

    return render(request, "guardarExcel.html", {"vinos": vinos})


def buscar(request):
    if request.GET["vino"]:
        producto = request.GET["vino"]
        botellas = Vino.objects.filter(nombre__icontains=producto) | Vino.objects.filter(cepas__icontains=producto)
        return render(request, "resultado.html", {"botellas":botellas, "query":producto} )
    else:
        return HttpResponse("Escribir la palabra a buscar")