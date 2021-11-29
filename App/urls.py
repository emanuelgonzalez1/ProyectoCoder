from django.urls import path
from App import views

urlpatterns = [
    path('', views.inicio),
    path('clientes/', views.clientes),
    path('profesionales/', views.profesinales),
    path('entregas/', views.entregas),
]
