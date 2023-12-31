from django.contrib import admin
from django.urls import include, path

from proyecto.views import inicio
from app_musicos.views import listar_musicos

urlpatterns = [
    path("admin/", admin.site.urls),
    path("musicos/", include("app_musicos.urls")),
    path("", inicio , name= "inicio"),
]
