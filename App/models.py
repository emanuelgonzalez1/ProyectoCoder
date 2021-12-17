from django.db import models

# Create your models here.
class Cliente(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.IntegerField()
    cuit = models.IntegerField()
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Telefono: {self.telefono} - Cuit: {self.cuit}'
    
class Profesional(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Profesión: {self.profesion}'
    
class Entrega(models.Model):
    
    nombre_entrega = models.CharField(max_length=50)
    fechadevencimiento = models.DateField()
    entregado = models.BooleanField()
    
    def __str__(self):
        return f'Nombre de entrega: {self.nombre_entrega} - Fecha límite: {self.fechadevencimiento} - Entregado: {self.entregado}'

