from django.urls import path
from App import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('profesionales/', views.profesinales, name='profesionales'),
    # path('entregas/', views.entregas, name='entregas'),
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
    path('crear_profesional/', views.crear_profesional, name='crear_profesional'),
    path('crear_entrega/', views.crear_entregas, name='crear_entrega'),
    path('busquedaCliente/', views.busquedaCliente, name='busquedaCliente'),
    path('buscar/', views.buscar),
    path('resultadoBusqueda/', views.buscar),
    path('clientelist', views.ClienteList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.ClienteDetail.as_view(), name='Detail'),
    path(r'^nuevo$', views.ClienteCreate.as_view(), name='Create'),
    path(r'^editar/(?P<pk>\d+)$', views.ClienteUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ClienteDelete.as_view(), name='Delete'),
    #prueba entrega
    path('entregalist', views.EntregaList.as_view(), name='EntregaList'),
    path(r'^(?P<pk>\d+)$', views.EntregaDetail.as_view(), name='EntregaDetail'),
    path(r'^nuevo$', views.EntregaCreate.as_view(), name='EntregaCreate'),
    path(r'^editar/(?P<pk>\d+)$', views.EntregaUpdate.as_view(), name='EntregaEdit'),
    path(r'^borrar/(?P<pk>\d+)$', views.EntregaDelete.as_view(), name='EntregaDelete'),
    path('login', views.login_request, name='Login'),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name = 'App/logout.html'), name = 'Logout'),
    path('editarperfil', views.editarperfil, name = "EditarPerfil"),
]
