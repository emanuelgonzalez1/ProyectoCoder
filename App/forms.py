from django import forms 

class clienteformulario (forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    telefono = forms.IntegerField()
    cuit = forms.IntegerField()
    
class profesionalformulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()
    
class entregasformulario(forms.Form):
    nombre_entrega = forms.CharField()
    fecha_limite = forms.DateField()
    entregado = forms.BooleanField()

