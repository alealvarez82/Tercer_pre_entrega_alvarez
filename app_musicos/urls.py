from django.urls import path
from app_musicos.views import (
    listar_instrumentos, crear_instrumento, eliminar_instrumento, listar_musicos, ver_nota, crear_nota, buscar_nota, crear_musico, eliminar_musico,
)
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q


urlpatterns = [
    path("instrumentos/", listar_instrumentos, name="listar_instrumentos"),
    path("crear-instrumento/", crear_instrumento, name="crear_instrumento"),
    path("eliminar-instrumento/<int:id>/", eliminar_instrumento, name="eliminar_instrumento"),
    #path("buscar-instrumento/", "listar_instrumentos", name="buscar_instrumento"),
    path("musicos/", listar_musicos, name="listar_musicos"),
    path("ingresar-musico/", crear_musico, name="crear_musico"),
    path("buscar-musico/", listar_musicos, name="buscar_musico"),
    path("eliminar-musico/<int:id>/", eliminar_musico, name="eliminar_musico"),
    path("ver-nota/", buscar_nota, name="ver_nota"),
    path("crear-nota/", crear_nota, name="crear_nota"),
    path("buscar-nota/", buscar_nota, name="buscar_nota"),
]
