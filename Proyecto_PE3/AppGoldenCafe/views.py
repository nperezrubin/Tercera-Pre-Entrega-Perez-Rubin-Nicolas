from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.


def inicio(req):
    return render(req, "appgoldencafe/padre.html")


def cliente(req):
    return render(req, "appgoldencafe/cliente.html")

def pedido(req):
    return render(req, "appgoldencafe/pedido.html")

def sucursal(req):
    return render(req, "appgoldencafe/sucursal.html")
