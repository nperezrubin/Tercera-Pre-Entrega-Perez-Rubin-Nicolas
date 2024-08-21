from django.shortcuts import render
from django.http import HttpResponse

from AppGoldenCafe.models import Cliente
from AppGoldenCafe.models import Pedido
from AppGoldenCafe.models import Sucursal

from AppGoldenCafe.forms import clienteFormulario
from AppGoldenCafe.forms import pedidoFormulario
from AppGoldenCafe.forms import sucursalFormulario

# Create your views here.


def inicio(req):
    return render(req, "appgoldencafe/padre.html")


def cliente(req):
    return render(req, "appgoldencafe/cliente.html")

def pedido(req):
    return render(req, "appgoldencafe/pedido.html")

def sucursal(req):
    return render(req, "appgoldencafe/sucursal.html")


#con html:
"""
def clienteFormulario(req):
    if req.method == 'POST':
        cliente = Cliente(nombre=req.POST['nombre'], email=req.POST['email'])
        cliente.save()
        return render(req, "AppGoldenCafe/padre.html")
    return render(req, "AppGoldenCafe/clienteFormulario.html")
"""

#con django:
def cliente_form_2(request):

    if request.method == "POST":
        miFormulario = clienteFormulario(request.POST) # creamos un objeto formulario con los datos enviados
        print(miFormulario) #para depuracion (opcional)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data   #obtenemos los datos limpios y validados
            cliente = Cliente(nombre = informacion["nombre"], email = informacion["email"]) #creamos un objeto Cliente
            cliente.save() #Guardamos el cliente en la BBDD
            return render(request, "AppGoldenCafe/padre.html") #redirigimos a la pagina de inicio
    else: # si es un GET...
        miFormulario = clienteFormulario() #creamos un formulario vacio para mostrarlo inicialmente
    return render(request, "AppGoldenCafe/cliente_form_2.html", {"miFormulario": miFormulario})



def pedido_form_2(request):

    if request.method == "POST":
        miFormulario = pedidoFormulario(request.POST) 
        print(miFormulario) 
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data   
            pedido = Pedido(tipo_cafe = informacion["tipo_cafe"], unidades = informacion["unidades"]) 
            pedido.save() 
            return render(request, "AppGoldenCafe/padre.html") 
    else:
        miFormulario = pedidoFormulario() 
    return render(request, "AppGoldenCafe/pedido_form_2.html", {"miFormulario": miFormulario})


def sucursal_form_2(request):

    if request.method == "POST":
        miFormulario = sucursalFormulario(request.POST) 
        print(miFormulario) 
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data   
            sucursal = Sucursal(barrio = informacion["barrio"], id_sucursal = informacion["id_sucursal"]) 
            sucursal.save() 
            return render(request, "AppGoldenCafe/padre.html") 
    else:
        miFormulario = sucursalFormulario() 
    return render(request, "AppGoldenCafe/sucursal_form_2.html", {"miFormulario": miFormulario})



def busquedaCliente(req):
    return render(req, "AppGoldenCafe/busquedaCliente.html")

def busquedaPedido(req):
    return render(req, "AppGoldenCafe/busquedaPedido.html")

def busquedaSucursal(req):
    return render(req, "AppGoldenCafe/busquedaSucursal.html")



def buscarcliente(req):
     if req.GET["nombre"]:
        #respuesta = f"Estoy buscando el cliente con nombre: {req.GET['nombre']}
        nombre = req.GET['nombre']
        clientes = Cliente.objects.filter(nombre__icontains=nombre)
        return render(req, "AppGoldenCafe/resultadoBusquedaCliente.html", {'clientes': clientes, 'nombre': nombre}) 
     else:
          respuesta= "No se enviaron datos"
    
     return HttpResponse(respuesta)


def buscarpedido(req):
     if req.GET["tipo_cafe"]:
        
        tipo_cafe = req.GET['tipo_cafe']
        pedidos = Pedido.objects.filter(tipo_cafe__icontains=tipo_cafe)
        return render(req, "AppGoldenCafe/resultadoBusquedaPedido.html", {'pedidos': pedidos, 'tipo_cafe': tipo_cafe}) 
     else:
          respuesta= "No se enviaron datos"
    
     return HttpResponse(respuesta)


def buscarsucursal(req):
     if req.GET["barrio"]:
        
        barrio = req.GET['barrio']
        sucursales = Sucursal.objects.filter(barrio__icontains=barrio)
        return render(req, "AppGoldenCafe/resultadoBusquedaSucursal.html", {'sucursales': sucursales, 'barrio': barrio}) 
     else:
          respuesta= "No se enviaron datos"
    
     return HttpResponse(respuesta)