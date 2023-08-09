from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="inicio"),
    path("recetas/", recetas, name="recetas"),
    path("cocineros/", cocineros, name="cocineros"),
    path("restaurantes/", restaurantes, name="restaurantes"),
    path("eliminar-receta/<int:id>", delete_receta, name="delete_receta"),
    path("eliminar-cocinero/<int:id>", delete_cocinero, name="delete_cocinero"),
    path("eliminar-restaurante/<int:id>", delete_restaurante, name="delete_restaurante"),
]
