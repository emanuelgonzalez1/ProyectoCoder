from django.db import models

# Create your models here.
class Cliente(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.IntegerField()
    cuit = models.IntegerField()
    
class Profesional(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    
class Entrega(models.Model):
    
    nombre_entrega = models.CharField(max_length=50)
    fechadevencimiento = models.DateField()
    entregado = models.BooleanField()

