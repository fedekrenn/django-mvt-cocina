from django.urls import path, include
from .views import *

urlpatterns = [
    path("", index, name="inicio"),
    path("recetas/", recetas, name="recetas"),
    path("cocineros/", cocineros, name="cocineros"),
    path("restaurantes/", restaurantes, name="restaurantes"),
]
