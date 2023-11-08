from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse('vista inicio')

def listar_instrumentos(request):
    return HttpResponse('vista instrumentos')

def listar_musicos(request):
    return HttpResponse('vista musicos')

def buscar_nota(request):
    return HttpResponse('vista notas')

def crear_nota(request):
    return HttpResponse('crear notas')