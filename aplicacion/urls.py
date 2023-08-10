from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="inicio"),
    path("recetas/", recetas, name="recetas"),
    path("cocineros/", cocineros, name="cocineros"),
    path("restaurantes/", restaurantes, name="restaurantes"),
    path("proveedores/", proveedores, name="proveedores"),
    path("acerca-de-mi/", acerca_de_mi, name="acerca_de_mi"),
    path("eliminar-receta/<int:id>", delete_receta, name="delete_receta"),
    path("eliminar-cocinero/<int:id>", delete_cocinero, name="delete_cocinero"),
    path("eliminar-restaurante/<int:id>", delete_restaurante, name="delete_restaurante"),
    path("eliminar-proveedor/<int:id>", delete_proveedor, name="delete_proveedor"),
    path("editar-receta/<int:id>", edit_receta, name="edit_receta"),
    path("editar-cocinero/<int:id>", edit_cocinero, name="edit_cocinero"),
    path("editar-restaurante/<int:id>", edit_restaurante, name="edit_restaurante"),
    path("editar-proveedor/<int:id>", edit_proveedor, name="edit_proveedor"),
]
