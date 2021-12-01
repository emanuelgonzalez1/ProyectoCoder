from django.shortcuts import render
from django.http import HttpResponse
from App.forms import clienteformulario
from App.models import Cliente



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

def crear_cliente(request):
    
    return render(request, 'App/crear_cliente.html')


cliente = None
def clienteformulario (request):
    if request.method == 'POST':
        formulario = clienteformulario(request.POST)
        
        if formulario.is_valid():
            datoscliente = formulario.cleaned_data
            cliente = Cliente (nombre = datoscliente['nombre'], apellido = datoscliente['apellido'], email = datoscliente['email'], cuit = datoscliente['cuit'])
            cliente.save()
        return render(request, 'App/index.html')
    else:
        formulario = clienteformulario()
    return render(request, 'App/crear_cliente.html', {'formulario': formulario})
