from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse('Hola!! Soy Manu')

def otravista(request):
    return HttpResponse('<h1>OTRA GRAN VISTA</h1>')

def fecha_actual(request):
    fecha_actual = datetime.now()
    return HttpResponse (f'<h1>{fecha_actual}</h1>')

def probandoTemplate(self):
    
    nombre = 'Emanuel'
    apellido = 'Gonzalez'
    mis_datos = {'nombre': nombre, 'apellido': apellido}
    # miHTML = open("Z:\CURSOS\Programacion\PYTHON\CODERHOUSEPYTHON\PROYECTO\ProyectoCoder\ProyectoCoder\plantillas\prueba.html")
    
    # plantilla = Template(miHTML.read())
    
    # miHTML.close()
    
    # miContexto = Context({'nombre': nombre, 'apellido': apellido})
    
    # documento = plantilla.render(miContexto)
    
    #otra forma mas facil que la de arriba es
    plantilla = loader.get_template('prueba.html')
    
    documento = plantilla.render(mis_datos)
    
    return HttpResponse(documento)
