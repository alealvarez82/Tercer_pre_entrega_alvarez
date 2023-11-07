from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    saludo = "Bienvenido a Blog del Musico"
    pagina_html = HttpResponse(saludo)
    return pagina_html

def musicos(request):
    conocer = "Conociendo a los musicos"
    pagina2_html = HttpResponse(conocer)
    return pagina2_html

def saludar_con_html(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='base.html',
        context=contexto,
    )
    return http_response