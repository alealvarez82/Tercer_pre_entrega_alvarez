from django.contrib import admin
from django.urls import path

from proyecto.views import saludar, saludar_con_html
from proyecto.views import musicos

urlpatterns = [
    path("admin/", admin.site.urls),
    path("saludo/", saludar),
    path("conocer/", musicos),
    path("inicio/", saludar_con_html),
]
