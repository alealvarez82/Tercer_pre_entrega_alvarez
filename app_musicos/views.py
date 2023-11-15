from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse

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
         "object_list": Musicos.objects.all()
    }
    http_response = render(
        request=request,
        template_name='app_musicos/listar_musicos.html',
        context=contexto,
    )
    return http_response

def ver_nota(request):
    return HttpResponse('vista notas')

def buscar_nota(request):
    return HttpResponse('vista notas')

def crear_nota(request):
    return HttpResponse('crear notas')

def crear_musico(request):
    if request.method == "POST":
        data = request.POST
        musico = Musicos(nombre=data['nombre'],
                         instrumento=data['instrumento'])
        musico.save()
        url_exitosa = reverse('listar_musicos')
        return redirect(url_exitosa)
    else:  # GET
        return render(
            request=request,
            template_name='app_musicos/crear_musico.html',
        )

def eliminar_musico(request, id):
    # obtienes el curso de la base de datos
    musicos = Musicos.objects.get(id=id)
    if request.method == "POST":
        # borra el curso de la base de datos
        musicos.delete()
        # redireccionamos a la URL exitosa
        url_exitosa = reverse('listar_musicos')
        return redirect(url_exitosa)


             

        

        
        