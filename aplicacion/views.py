from django.shortcuts import render
from .models import Receta, Cocinero, Restaurante, Proveedor
from .forms import RecetaForm, CocineroForm, RestauranteForm, ProveedorForm


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


def acerca_de_mi(request):
    return render(request, "aplicacion/acerca-de-mi.html")


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


def edit_receta(request, id):
    receta = Receta.objects.get(id=id)
    if request.method == "POST":
        form = RecetaForm(request.POST)
        if form.is_valid():
            receta.nombre = form.cleaned_data["nombre"]
            receta.ingredientes = form.cleaned_data["ingredientes"]
            receta.tiempo = form.cleaned_data["tiempo"]
            receta.dificultad = form.cleaned_data["dificultad"]
            receta.save()

            return render(request, "aplicacion/confirmacion-guardado.html")
    else:
        form = RecetaForm(
            initial={
                "nombre": receta.nombre,
                "ingredientes": receta.ingredientes,
                "tiempo": receta.tiempo,
                "dificultad": receta.dificultad,
            }
        )

    ctx = {"recetas": Receta.objects.all(), "form": form}

    return render(request, "aplicacion/editar.html", ctx)


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


def edit_cocinero(request, id):
    cocinero = Cocinero.objects.get(id=id)
    if request.method == "POST":
        form = CocineroForm(request.POST)
        if form.is_valid():
            cocinero.nombre = form.cleaned_data["nombre"]
            cocinero.apellido = form.cleaned_data["apellido"]
            cocinero.edad = form.cleaned_data["edad"]
            cocinero.especialidad = form.cleaned_data["especialidad"]
            cocinero.save()

            return render(request, "aplicacion/confirmacion-guardado.html")
    else:
        form = CocineroForm(
            initial={
                "nombre": cocinero.nombre,
                "apellido": cocinero.apellido,
                "edad": cocinero.edad,
                "especialidad": cocinero.especialidad,
            }
        )

    ctx = {"cocineros": Cocinero.objects.all(), "form": form}

    return render(request, "aplicacion/editar.html", ctx)


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


def edit_restaurante(request, id):
    restaurante = Restaurante.objects.get(id=id)
    if request.method == "POST":
        form = RestauranteForm(request.POST)
        if form.is_valid():
            restaurante.nombre = form.cleaned_data["nombre"]
            restaurante.direccion = form.cleaned_data["direccion"]
            restaurante.telefono = form.cleaned_data["telefono"]
            restaurante.categoria = form.cleaned_data["categoria"]
            restaurante.save()

            return render(request, "aplicacion/confirmacion-guardado.html")
    else:
        form = RestauranteForm(
            initial={
                "nombre": restaurante.nombre,
                "direccion": restaurante.direccion,
                "telefono": restaurante.telefono,
                "categoria": restaurante.categoria,
            }
        )

    ctx = {"restaurantes": Restaurante.objects.all(), "form": form}

    return render(request, "aplicacion/editar.html", ctx)


def proveedores(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            telefono = form.cleaned_data["telefono"]
            email = form.cleaned_data["email"]
            producto = form.cleaned_data["producto"]

            Proveedor.objects.create(
                nombre=nombre, telefono=telefono, email=email, producto=producto
            )

            return render(request, "aplicacion/confirmacion-guardado.html")
    else:
        form = ProveedorForm()

    ctx = {"proveedores": Proveedor.objects.all(), "form": form}
    return render(request, "aplicacion/proveedores.html", ctx)


def delete_proveedor(request, id):
    Proveedor.objects.get(id=id).delete()
    return render(request, "aplicacion/confirmacion-eliminado.html")


def edit_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            proveedor.nombre = form.cleaned_data["nombre"]
            proveedor.telefono = form.cleaned_data["telefono"]
            proveedor.email = form.cleaned_data["email"]
            proveedor.producto = form.cleaned_data["producto"]
            proveedor.save()

            return render(request, "aplicacion/confirmacion-guardado.html")
    else:
        form = ProveedorForm(
            initial={
                "nombre": proveedor.nombre,
                "telefono": proveedor.telefono,
                "email": proveedor.email,
                "producto": proveedor.producto,
            }
        )

    ctx = {"proveedores": Proveedor.objects.all(), "form": form}

    return render(request, "aplicacion/editar.html", ctx)
