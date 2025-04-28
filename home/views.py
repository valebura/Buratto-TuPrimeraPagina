from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import CreacionProfesional, CreacionCortePelo, CreacionCliente
from home.models import Profesional, CortePelo, Cliente
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'inicio.html')


# --------------- PROFESIONALES ---------------

@login_required
def crear_profesional(request):
    
    if request.method == "POST":
        formulario = CreacionProfesional(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            profesional = Profesional(nombre=info.get('nombre'), apellido=info.get('apellido'), anos_experiencia=info.get('anos_experiencia'))
            profesional.save()
            return redirect('listado_profesionales')
    else:
        formulario = CreacionProfesional()
        
    return render(request, 'profesionales/crear_profesional.html', {'formulario': formulario})
class DetalleProfesional(DetailView):
    model = Profesional
    template_name = "profesionales/detalle_profesional.html"

class ModificarProfesional(LoginRequiredMixin, UpdateView):
    model = Profesional
    template_name = "profesionales/modificar_profesional.html"
    fields = ["nombre", "apellido", "anos_experiencia"]
    success_url = reverse_lazy("listado_profesionales")

class EliminarProfesional(LoginRequiredMixin, DeleteView):
    model = Profesional
    template_name = "profesionales/eliminar_profesional.html"
    success_url = reverse_lazy("listado_profesionales")
    
def listado_profesionales(request):
    profesionales = Profesional.objects.all()
    return render(request, 'profesionales/listado_profesionales.html', {'profesionales': profesionales})
    


# --------------- CORTES DE PELO ---------------

@login_required
def crear_corte_pelo(request):
    
    if request.method == "POST":
        formulario = CreacionCortePelo(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            corte_pelo = CortePelo(nombre=info.get('nombre'), precio=info.get('precio'), tiempo=info.get('tiempo'))
            corte_pelo.save()
            return redirect('listado_cortes_pelo')
    else:
        formulario = CreacionCortePelo()
        
    return render(request, 'cortes_pelo/crear_corte_pelo.html', {'formulario': formulario})

class DetalleCortePelo(DetailView):
    model = CortePelo
    template_name = "cortes_pelo/detalle_corte_pelo.html"

class ModificarCortePelo(LoginRequiredMixin, UpdateView):
    model = CortePelo
    template_name = "cortes_pelo/modificar_corte_pelo.html"
    fields = ["nombre", "precio", "tiempo"]
    success_url = reverse_lazy("listado_cortes_pelo")

class EliminarCortePelo(LoginRequiredMixin, DeleteView):
    model = CortePelo
    template_name = "cortes_pelo/eliminar_corte_pelo.html"
    success_url = reverse_lazy("listado_cortes_pelo")

def listado_cortes_pelo(request):
    cortes_pelo = CortePelo.objects.all()
    return render(request, 'cortes_pelo/listado_cortes_pelo.html', {'cortes_pelo': cortes_pelo})



# --------------- CLIENTES ---------------

@login_required
def crear_cliente(request):
    
    if request.method == "POST":
        formulario = CreacionCliente(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            cliente = Cliente(nombre=info.get('nombre'), apellido=info.get('apellido'), email=info.get('email'))
            cliente.save()
            return redirect('listado_clientes')
    else:
        formulario = CreacionCliente()
        
    return render(request, 'clientes/crear_cliente.html', {'formulario': formulario})

class DetalleCliente(DetailView):
    model = Cliente
    template_name = "clientes/detalle_cliente.html"

class ModificarCliente(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = "clientes/modificar_cliente.html"
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("listado_clientes")

class EliminarCliente(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = "clientes/eliminar_cliente.html"
    success_url = reverse_lazy("listado_clientes")

def listado_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listado_clientes.html', {'clientes': clientes})