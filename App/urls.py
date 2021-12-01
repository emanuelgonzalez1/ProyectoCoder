from django.urls import path
from App import views

urlpatterns = [
    path('', views.inicio, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('profesionales/', views.profesinales, name='profesionales'),
    path('entregas/', views.entregas, name='entregas'),
    path('link4/', views.link4, name='link4'),
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
]
