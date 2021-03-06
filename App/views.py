from django.shortcuts import render
from django.http import HttpResponse
from App.forms import clienteformulario, entregasformulario, profesionalformulario, RegistroUsuarioForm, UserEditForm
from App.models import Cliente, Entrega, Profesional
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
def inicio(request):
    
    return render(request, 'App/index.html')

def clientes(request):
    
    return render(request, 'App/clientes.html')

def profesinales(request):
    
    return render(request, 'App/profesionales.html')

def entregas(request):
    
    return render(request, 'App/entregas.html')


#def crear_cliente(request):
#   
#    return render(request, 'App/crear_cliente.html')


cliente = None
def crear_cliente (request):
    if request.method == 'POST':
        formulario = clienteformulario(request.POST)
        
        if formulario.is_valid():
            datoscliente = formulario.cleaned_data
            cliente = Cliente (nombre = datoscliente['nombre'], apellido = datoscliente['apellido'], telefono = datoscliente['telefono'], cuit = datoscliente['cuit'])
            cliente.save()
        return render(request, 'App/index.html')
    else:
        formulario = clienteformulario()
    return render(request, 'App/crear_cliente.html', {'formulario': formulario})

profesional = None
def crear_profesional (request):
    if request.method == 'POST':
        formulario1 = profesionalformulario(request.POST)
        
        if formulario1.is_valid():
            datosprofesional = formulario1.cleaned_data
            profesional = Profesional (nombre = datosprofesional['nombre'], apellido = datosprofesional['apellido'], email = datosprofesional['email'], profesion = datosprofesional['profesion'])
            profesional.save()
        return render (request, 'App/index.html')
    else:
        formulario1 = profesionalformulario()
    return render(request, 'App/crear_profesional.html', {'formulario1':formulario1})

entregas = None
def crear_entregas(request):
    if request.method == 'POST':
        formulario2 = entregasformulario(request.POST)
        
        if formulario2.is_valid():
            datosentrega = formulario2.cleaned_data
            entrega = Entrega (nombre_entrega = datosentrega['nombre_entrega'], fechadevencimiento = datosentrega['fecha_limite'], entregado = datosentrega['entregado'])
            entrega.save()
        return render(request, 'App/index.html')
    else:
        formulario2 = entregasformulario()
    return render(request, 'App/crear_entrega.html', {'formulario2':formulario2})

def busquedaCliente(request):
    
    return render (request, "App/busquedaCliente.html")

def buscar(request):
    
    if request.GET['cuit']:
        cuit=request.GET['cuit']
        cliente = Cliente.objects.filter(cuit__icontains= cuit)
        
        return render (request, 'App/resultadoBusqueda.html', {'cliente':cliente, 'cuit':cuit})
    
    else:
        respuesta = 'No enviaste ningun dato'
        
    return HttpResponse(respuesta)

class EntregaList(ListView):
    model = Entrega
    template_name = 'App/entrega_list.html'
    
class EntregaDetail(DetailView):
    model = Entrega
    template_name = 'App/entrega_detail.html'
    
class EntregaCreate(CreateView):
    model = Entrega
    success_url = 'App/entregalist'
    fields = ['nombre_entrega', 'fechadevencimiento', 'entregado']
    
class EntregaUpdate(UpdateView):
    model = Entrega
    success_url = 'App/entregalist'
    fields = ['nombre_entrega', 'fechadevencimiento', 'entregado']
    
class EntregaDelete(DeleteView):
    model = Entrega
    success_url = 'App/entregalist'
class ClienteList(ListView):
    model = Cliente
    template_name = 'App/cliente_list.html'
    
class ClienteDetail(DetailView):
    model = Cliente
    template_name = 'App/cliente_detail.html'
    
class ClienteCreate(CreateView):
    model = Cliente
    success_url = 'App/clientelist'
    fields = ['nombre', 'apellido', 'telefono', 'cuit']
    
class ClienteUpdate(UpdateView):
    model = Cliente
    success_url = 'App/clientelist'
    fields = ['nombre', 'apellido', 'telefono', 'cuit']
    
class ClienteDelete(DeleteView):
    model = Cliente
    success_url = 'App/clientelist'
    
def login_request(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrase??a = form.cleaned_data.get('password')
            
            user = authenticate(username = usuario, password = contrase??a)
            
            if user is not None:
                login(request, user)
                
                return render(request, 'App/index.html', {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, 'App/index.html', {"mensaje": "Error, datos incorrectos"})
        else:
                return render(request, 'App/index.html', {"mensaje": "Error, formulario erroneo"})
            
    form = AuthenticationForm()
    
    return render (request,'App/login.html', {'form': form })


def register (request):
    
    if request.method == 'POST':
        
        form = RegistroUsuarioForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data['username']
            form.save()
            return render (request, 'App/index.html', {"mensaje":"Usuario Creado :D"})
    
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'App/registro.html',{"form": form})
            

@login_required
def editarperfil(request):
    
    usuario = request.user
    
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            
            return render (request, "App/index.html")
    
    else:
        miFormulario = UserEditForm(initial = {'email':usuario.email})
    
    return render(request, "App/editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})
            