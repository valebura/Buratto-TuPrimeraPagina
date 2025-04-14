from django.urls import path
from home.views import inicio, crear_profesional, listado_profesionales, crear_corte_pelo, listado_cortes_pelo, crear_cliente, listado_clientes

urlpatterns = [
    path('', inicio, name='inicio'),
    path('profesionales/', listado_profesionales, name='listado_profesionales'),
    path('cortes_pelo/', listado_cortes_pelo, name='listado_cortes_pelo'),
    path('clientes/', listado_clientes, name='listado_clientes'),
    path('profesionales/crear', crear_profesional, name='crear_profesional'),
    path('cortes_pelo/crear', crear_corte_pelo, name='crear_corte_pelo'),
    path('clientes/crear', crear_cliente, name='crear_cliente'),
]
