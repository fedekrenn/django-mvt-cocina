from django.shortcuts import render
from django.http import HttpResponse
from .models import Receta, Cocinero, Restaurante


# Create your views here.
def index(request):
    return render(request, "aplicacion/index.html")


def recetas(request):
    ctx = { "recetas": Receta.objects.all() }
    return render(request, "aplicacion/recetas.html", ctx)


def cocineros(request):
    ctx = { "cocineros": Cocinero.objects.all() }
    return render(request, "aplicacion/cocineros.html", ctx)


def restaurantes(request):
    ctx = { "restaurantes": Restaurante.objects.all() }
    return render(request, "aplicacion/restaurante.html", ctx)
