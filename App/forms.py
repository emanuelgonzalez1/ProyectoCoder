from django import forms 

class clienteformulario (forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    cuit = forms.IntegerField()
    
class profesionalformulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    
class entregasformulario(forms.Form):
    nombre_entrega = forms.CharField()
    fecha_limite = forms.DateField()
    entregado = forms.BooleanField()

