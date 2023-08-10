from django import forms


class RecetaForm(forms.Form):
    nombre = forms.CharField(label="Nombre de la receta", max_length=50, required=True)
    ingredientes = forms.CharField(label="Ingredientes", max_length=50, required=True)
    tiempo = forms.IntegerField(label="Tiempo de preparación en minutos", required=True)
    DIFICULTAD = (
        (1, "Fácil"),
        (2, "Media"),
        (3, "Difícil"),
    )
    dificultad = forms.ChoiceField(
        label="Dificultad", choices=DIFICULTAD, required=True
    )


class CocineroForm(forms.Form):
    nombre = forms.CharField(label="Nombre del cocinero", max_length=50, required=True)
    apellido = forms.CharField(
        label="Apellido del cocinero", max_length=50, required=True
    )
    edad = forms.IntegerField(label="Edad", required=True)
    especialidad = forms.CharField(label="Especialidad del cocinero", max_length=50)


class RestauranteForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre del restaurante", max_length=50, required=True
    )
    direccion = forms.CharField(label="Dirección", max_length=50, required=True)
    telefono = forms.CharField(
        label="Teléfono del contacto", max_length=50, required=True
    )
    CATEGORIA = (
        ("Comida rápida", "Comida rápida"),
        ("Meriendas", "Meriendas"),
        ("Veggie", "Veggie"),
        ("Cena", "Cena"),
    )
    categoria = forms.ChoiceField(label="Categoría", choices=CATEGORIA, required=True)


class ProveedorForm(forms.Form):
    nombre = forms.CharField(label="Nombre del proveedor", max_length=50, required=True)
    telefono = forms.CharField(
        label="Teléfono del contacto", max_length=50, required=True
    )
    email = forms.CharField(label="Email", max_length=50, required=True)

    PRODUCTO = (
        ("Carnes", "Carnes"),
        ("Verdura", "Verdura"),
        ("Bebidas", "Bebidas"),
        ("Pescado", "Pescado"),
        ("Postres", "Postres"),
        ("Pan", "Pan"),
    )
    producto = forms.ChoiceField(label="Producto", choices=PRODUCTO, required=True)
