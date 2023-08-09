from django.shortcuts import render
from django.http import HttpResponse
from .models import Receta, Cocinero, Restaurante
from .forms import RecetaForm, CocineroForm, RestauranteForm


# Create your views here.
def index(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        recetas = Receta.objects.filter(nombre__contains=nombre)
        ctx = {"recetas": recetas}

        if not recetas:
            ctx = {"error": "No se encontraron recetas con ese nombre"}

        return render(request, "aplicacion/index.html", ctx)

    return render(request, "aplicacion/index.html")


def recetas(request):
    if request.method == "POST":
        form = RecetaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            ingredientes = form.cleaned_data["ingredientes"]
            tiempo = form.cleaned_data["tiempo"]
            dificultad = form.cleaned_data["dificultad"]

            Receta.objects.create(
                nombre=nombre,
                ingredientes=ingredientes,
                tiempo=tiempo,
                dificultad=dificultad,
            )

            return render(request, "aplicacion/confirmacion-guardado.html")
    else:
        form = RecetaForm()

    ctx = {"recetas": Receta.objects.all(), "form": form}

    return render(request, "aplicacion/recetas.html", ctx)


def delete_receta(request, id):
    Receta.objects.get(id=id).delete()
    return render(request, "aplicacion/confirmacion-eliminado.html")


def cocineros(request):
    if request.method == "POST":
        form = CocineroForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            edad = form.cleaned_data["edad"]
            especialidad = form.cleaned_data["especialidad"]

            Cocinero.objects.create(
                nombre=nombre, apellido=apellido, edad=edad, especialidad=especialidad
            )

            return render(request, "aplicacion/confirmacion-guardado.html")
    else:
        form = CocineroForm()

    ctx = {"cocineros": Cocinero.objects.all(), "form": form}
    return render(request, "aplicacion/cocineros.html", ctx)


def delete_cocinero(request, id):
    Cocinero.objects.get(id=id).delete()
    return render(request, "aplicacion/confirmacion-eliminado.html")


def restaurantes(request):
    if request.method == "POST":
        form = RestauranteForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            direccion = form.cleaned_data["direccion"]
            telefono = form.cleaned_data["telefono"]
            categoria = form.cleaned_data["categoria"]

            Restaurante.objects.create(
                nombre=nombre,
                direccion=direccion,
                telefono=telefono,
                categoria=categoria,
            )

            return render(request, "aplicacion/confirmacion-guardado.html")
    else:
        form = RestauranteForm()

    ctx = {"restaurantes": Restaurante.objects.all(), "form": form}
    return render(request, "aplicacion/restaurante.html", ctx)


def delete_restaurante(request, id):
    Restaurante.objects.get(id=id).delete()
    return render(request, "aplicacion/confirmacion-eliminado.html")
