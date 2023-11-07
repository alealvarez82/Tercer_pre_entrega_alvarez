from django.urls import path
from app_musicos.views import *

urlpatterns = [
    path("instrumentos/", listar_instrumentos(), name="lista_instrumentos"),
    path("musicos/", listar_musicos(), name="lista_musicos"),
    path("crear-nota/", crear_nota(), name="crear_nota"),
    path("buscar-nota/", buscar_nota(), name="buscar_nota"),
]
