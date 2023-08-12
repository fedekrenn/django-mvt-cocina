from django.contrib import admin
from .models import Cocinero, Receta, Restaurante, Proveedor

# Register your models here.
admin.site.register(Cocinero)
admin.site.register(Receta)
admin.site.register(Restaurante)
admin.site.register(Proveedor)
