from django.db import models

# Create your models here.

class Cliente(models.Model):   
    nombre = models.CharField(max_length=30)
    email = models.EmailField()


class Pedido(models.Model):   
    tipo_cafe = models.CharField(max_length=30)
    unidades = models.IntegerField()


class Sucursal(models.Model):   
    barrio = models.CharField(max_length=30)
    id_sucursal = models.IntegerField()