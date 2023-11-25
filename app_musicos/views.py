from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.db.models import Q

from app_musicos.forms import MusicoFormulario
from app_musicos.models import Musicos, Instrumentos

# Create your views here.

def listar_instrumentos(request):
    contexto = {
         "object_list": Instrumentos.objects.all()
    }
    http_response = render(
        request=request,
        template_name='app_musicos/listar_instrumentos.html',
        context=contexto,
    )
    return http_response


def crear_instrumento(request):
    if request.method == "POST":
        data = request.POST
        instrumento = Instrumentos(instrumento=data['instrumento'],
                         tipo=data['tipo'])
        instrumento.save()
        url_exitosa = reverse('listar_instrumentos')
        return redirect(url_exitosa)
    else:  # GET
        return render(
            request=request,
            template_name='app_musicos/crear_instrumento.html',
        )

def eliminar_instrumento(request, id):
    instrumento = Instrumentos.objects.get(id=id)
    if request.method == "POST":
       instrumento.delete()
       url_exitosa = reverse('listar_instrumentos')
       return redirect(url_exitosa)


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
    musico = Musicos.objects.get(id=id)
    if request.method == "POST":
       musico.delete()
       url_exitosa = reverse('listar_musicos')
       return redirect(url_exitosa)
    
def editar_musico(request, id):
   musico = Musicos.objects.get(id=id)
   if request.method == "POST":
       formulario = MusicoFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           musico.nombre = data['nombre']
           musico.instrumento = data['instrumento']
           musico.save()
           url_exitosa = reverse('listar_musicos')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': musico.nombre,
           'instrumento': musico.instrumento,
       }
       formulario = MusicoFormulario(initial=inicial)
   return render(
       request=request,
       template_name='app_musicos/musico_form.html',
       context={'formulario': formulario},
   )

def ver_nota(request):
    return HttpResponse('vista notas')

def buscar_nota(request):
    return HttpResponse('vista notas')

def crear_nota(request):
    return HttpResponse('crear notas')

             

        

        
        