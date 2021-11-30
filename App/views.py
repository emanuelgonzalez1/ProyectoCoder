from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def inicio(request):
    
    return render(request, 'App/index.html')

def clientes(request):
    
    return render(request, 'App/clientes.html')

def profesinales(request):
    
    return render(request, 'App/profesionales.html')

def entregas(request):
    
    return render(request, 'App/entregas.html')

def link4(request):
    
    return render(request, 'App/link4.html')