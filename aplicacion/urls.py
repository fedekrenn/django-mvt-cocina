from django.urls import path
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", index, name="inicio"),
    path("login/", login_request, name="login"),
    path("logout/", LogoutView.as_view(template_name="aplicacion/sesion/logout.html"), name="logout"),
    path("register/", register, name="registro"),
    path("editar-perfil/", edit_profile, name="editar_perfil"),
    path("cambiar-password/", change_pass, name="cambiar_password"),
    path("agregar-avatar", add_avatar, name="agregar_avatar"),
    path("recetas/", recetas, name="recetas"),
    path("cocineros/", cocineros, name="cocineros"),
    path("restaurantes/", restaurantes, name="restaurantes"),
    path("proveedores/", proveedores, name="proveedores"),
    path("acerca-de-mi/", acerca_de_mi, name="acerca_de_mi"),
    path("eliminar-receta/<int:pk>", RecetaDelete.as_view(), name="delete_receta"),
    path("eliminar-cocinero/<int:pk>", CocineroDelete.as_view(), name="delete_cocinero"),
    path("eliminar-restaurante/<int:pk>", RestauranteDelete.as_view(), name="delete_restaurante"),
    path("eliminar-proveedor/<int:pk>", ProveedorDelete.as_view(), name="delete_proveedor"),
    path("editar-receta/<int:pk>", RecetaUpdate.as_view(), name="edit_receta"),
    path("editar-cocinero/<int:pk>", CocineroUpdate.as_view(), name="edit_cocinero"),
    path("editar-restaurante/<int:pk>", RestauranteUpdate.as_view(), name="edit_restaurante"),
    path("editar-proveedor/<int:pk>", ProveedorUpdate.as_view(), name="edit_proveedor"),
    path("detalle-receta/<int:pk>", RecetaDetail.as_view(), name="detail_receta"),
    path("detalle-cocinero/<int:pk>", CocineroDetail.as_view(), name="detail_cocinero"),
    path("detalle-restaurante/<int:pk>", RestauranteDetail.as_view(), name="detail_restaurante"),
    path("detalle-proveedor/<int:pk>", ProveedorDetail.as_view(), name="detail_proveedor"),
]
