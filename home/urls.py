from django.urls import path
from home.views import inicio, crear_profesional, detalle_profesional, DetalleProfesional, ModificarProfesional, EliminarProfesional, listado_profesionales, crear_corte_pelo, listado_cortes_pelo, crear_cliente, listado_clientes

urlpatterns = [
    path('', inicio, name='inicio'),
    
    # Profesionales
    path('profesionales/', listado_profesionales, name='listado_profesionales'),
    path('profesionales/crear', crear_profesional, name='crear_profesional'),
    # path('profesionales/<int:profesional_especifico>/', detalle_profesional, name='detalle_profesional'),
    path('profesionales/<int:pk>', DetalleProfesional.as_view(), name='detalle_profesional'),
    path('profesionales/<int:pk>/modificar', ModificarProfesional.as_view(), name='modificar_profesional'),
    path('profesionales/<int:pk>/eliminar', EliminarProfesional.as_view(), name='eliminar_profesional'),
    
    # Cortes de pelo
    path('cortes_pelo/', listado_cortes_pelo, name='listado_cortes_pelo'),
    path('cortes_pelo/crear', crear_corte_pelo, name='crear_corte_pelo'),
    
    # Clientes
    path('clientes/', listado_clientes, name='listado_clientes'),
    path('clientes/crear', crear_cliente, name='crear_cliente'),
]
