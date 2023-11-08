from django.urls import path
from app_musicos.views import *

urlpatterns = [
    path("instrumentos/", listar_instrumentos(), name="lista_instrumentos"),
    path("ingresar-instrumento/", listar_instrumentos(), name="ingresar_instrumento"),
    path("buscar-instrumento/", listar_instrumentos(), name="buscar_instrumento"),
    path("musicos/", listar_musicos(), name="lista_musicos"),
    path("ingresar-musico/", listar_musicos(), name="ingresar_musico"),
    path("buscar-musico/", listar_musicos(), name="buscar_musico"),
    path("ver-nota/", buscar_nota(), name="ver_nota"),
    path("crear-nota/", crear_nota(), name="crear_nota"),
    path("buscar-nota/", buscar_nota(), name="buscar_nota"),
]
