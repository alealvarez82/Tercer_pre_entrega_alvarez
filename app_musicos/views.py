from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse('vista inicio')

def instrumentos(request):
    return HttpResponse('vista instrumentos')

def musicos(request):
    return HttpResponse('vista musicos')

def notas(request):
    return HttpResponse('vista notas')