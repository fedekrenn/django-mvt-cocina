from django.shortcuts import render
from django.http import HttpResponse
from .models import Receta, Cocinero, Restaurante


# Create your views here.
def index(request):
    return render(request, "aplicacion/index.html")


def recetas(request):
    return render(request, "aplicacion/recetas.html")


def cocineros(request):
    return render(request, "aplicacion/cocineros.html")


def restaurantes(request):
    return render(request, "aplicacion/restaurantes.html")
