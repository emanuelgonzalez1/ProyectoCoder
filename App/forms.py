from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField 
from django.contrib.auth.models import User
from django.forms import fields
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

class RegistroUsuarioForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    last_name = forms.CharField()
    first_name = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'last_name', 'first_name']
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='Modificar Email')
    password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget= forms.PasswordInput)
    
    class Meta:
        model = User
        fields= ['email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
        