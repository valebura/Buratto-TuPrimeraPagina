from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import CreacionProfesional, CreacionCortePelo, CreacionCliente
from home.models import Profesional, CortePelo, Cliente

def inicio(request):
    return render(request, 'inicio.html')

def listado_profesionales(request):
    profesionales = Profesional.objects.all()
    return render(request, 'listado_profesionales.html', {'profesionales': profesionales})

def listado_cortes_pelo(request):
    cortes_pelo = CortePelo.objects.all()
    return render(request, 'listado_cortes_pelo.html', {'cortes_pelo': cortes_pelo})

def listado_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listado_clientes.html', {'clientes': clientes})

def crear_profesional(request):
    
    print(request.GET)
    print(request.POST)
    
    if request.method == "POST":
        formulario = CreacionProfesional(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            profesional = Profesional(nombre=info.get('nombre'), apellido=info.get('apellido'), anos_experiencia=info.get('anos_experiencia'))
            profesional.save()
            return redirect('listado_profesionales')
    else:
        formulario = CreacionProfesional()
        
    return render(request, 'crear_profesional.html', {'formulario': formulario})

def crear_corte_pelo(request):
    
    print(request.GET)
    print(request.POST)
    
    if request.method == "POST":
        formulario = CreacionCortePelo(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            corte_pelo = CortePelo(nombre=info.get('nombre'), precio=info.get('precio'), tiempo=info.get('tiempo'))
            corte_pelo.save()
            return redirect('listado_cortes_pelo')
    else:
        formulario = CreacionCortePelo()
        
    return render(request, 'crear_corte_pelo.html', {'formulario': formulario})

def crear_cliente(request):
    
    print(request.GET)
    print(request.POST)
    
    if request.method == "POST":
        formulario = CreacionCliente(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            cliente = Cliente(nombre=info.get('nombre'), apellido=info.get('apellido'), email=info.get('email'))
            cliente.save()
            return redirect('listado_clientes')
    else:
        formulario = CreacionCliente()
        
    return render(request, 'crear_cliente.html', {'formulario': formulario})