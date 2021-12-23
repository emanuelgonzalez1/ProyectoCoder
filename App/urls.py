from django.urls import path
from App import views

urlpatterns = [
    path('', views.inicio, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('profesionales/', views.profesinales, name='profesionales'),
    # path('entregas/', views.entregas, name='entregas'),
    path('link4/', views.link4, name='link4'),
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
    path('crear_profesional/', views.crear_profesional, name='crear_profesional'),
    path('crear_entrega/', views.crear_entregas, name='crear_entrega'),
    path('busquedaCliente/', views.busquedaCliente, name='busquedaCliente'),
    path('buscar/', views.buscar),
    path('resultadoBusqueda/', views.buscar),
    path('cliente/list', views.ClienteList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.ClienteDetail.as_view(), name='Detail'),
    path(r'^nuevo$', views.ClienteCreate.as_view(), name='Create'),
    path(r'^editar/(?P<pk>\d+)$', views.ClienteUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ClienteDelete.as_view(), name='Delete'),
]
