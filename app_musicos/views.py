from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from app_musicos.models import Instrumentos, Musicos, Notas

# Create your views here.

def listar_instrumentos(request):
    return HttpResponse('vista instrumentos')

def ingresar_instrumento(request):
    return HttpResponse('vista instrumentos')

def buscar_instrumento(request):
    return HttpResponse('vista instrumentos')



def listar_musicos(request):
    contexto = {
        "Creador" : "Ale VH"
    }
    http_response = render(
        request=request,
        template_name='app_musicos/listar_musicos.html',
        context=contexto,
    )
    return http_response

def ingresar_musico(request):
    return HttpResponse('vista musicos')

def ver_nota(request):
    return HttpResponse('vista notas')

def buscar_nota(request):
    return HttpResponse('vista notas')

def crear_nota(request):
    return HttpResponse('crear notas')