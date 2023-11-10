from django.contrib import admin
from django.urls import include, path

from proyecto.views import saludar_con_html
from app_musicos.views import listar_musicos

urlpatterns = [
    path("admin/", admin.site.urls),
    path("musicos/", include("app_musicos.urls")),
    path("", saludar_con_html, name="inicio"),
]
