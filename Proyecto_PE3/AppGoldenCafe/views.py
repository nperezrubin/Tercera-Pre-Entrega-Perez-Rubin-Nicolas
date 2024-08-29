from django.shortcuts import render, redirect
from django.http import HttpResponse

from AppGoldenCafe.models import Cliente, Pedido, Sucursal
from AppGoldenCafe.forms import clienteFormulario, pedidoFormulario, sucursalFormulario



def inicio(req):
    return redirect('homepage')

def homepage(req):
    return render(req, "appgoldencafe/padre.html")


#def cliente(req):
#    return render(req, "appgoldencafe/cliente.html")

#def pedido(req):
#    return render(req, "appgoldencafe/pedido.html")

#def sucursal(req):
#    return render(req, "appgoldencafe/sucursal.html")


def cliente(request):
    clientes = Cliente.objects.all()
    miFormulario = clienteFormulario()
    if request.method == "POST":
        
        if 'agregar_cliente' in request.POST:
            miFormulario = clienteFormulario(request.POST)  # creamos un objeto formulario con los datos enviados
            if miFormulario.is_valid():
                cliente = Cliente(nombre=miFormulario.cleaned_data['nombre'], email=miFormulario.cleaned_data['email']) #creo el objeto Cliente ya limpio
                cliente.save()                              # Guardamos el cliente en la BBDD
                return redirect('clientes')                 # redirigimos a clientes
            else:
                return render(request, "AppGoldenCafe/cliente.html", {'form': miFormulario})
            
        elif 'buscar_cliente' in request.POST:
            miFormulario = clienteFormulario()
            nombre = request.POST.get('nombre')
            if nombre:                       # respuesta = f"Estoy buscando el cliente con nombre: {req.GET['nombre']}
                clientes = Cliente.objects.filter(nombre__iexact=nombre)
                if clientes:
                    return render(request,"AppGoldenCafe/cliente.html", {'clientes': clientes, 'nombre': nombre})
                else:
                    mensaje = "El cliente ingresado no existe."
                    return render(request, "AppGoldenCafe/cliente.html", {'mensaje': mensaje, 'form': miFormulario})
            else:
                mensaje = "Por favor, ingresa un nombre para buscar."
                return render(request, "AppGoldenCafe/cliente.html", {'mensaje': mensaje, 'form': miFormulario})
        else:
            miFormulario = clienteFormulario()
            return render(request, "AppGoldenCafe/cliente.html", {'form': miFormulario})
               
    else:                                                   # si es un GET...
        miFormulario = clienteFormulario()                  # creamos un formulario vacio para mostrarlo inicialmente
        return render(request, "AppGoldenCafe/cliente.html", {'clientes': clientes, 'form': miFormulario})



def pedido(request):
    pedidos = Pedido.objects.all()
    miFormulario = pedidoFormulario()
    if request.method == "POST":
        
        if 'agregar_pedido' in request.POST:
            miFormulario = pedidoFormulario(request.POST)  
            if miFormulario.is_valid():
                pedido = Pedido(tipo_cafe=miFormulario.cleaned_data['tipo_cafe'], unidades=miFormulario.cleaned_data['unidades']) 
                pedido.save()                             
                return redirect('pedidos')                 
            else:
                return render(request, "AppGoldenCafe/pedido.html", {'form': miFormulario})
            
        elif 'buscar_pedido' in request.POST:
            miFormulario = pedidoFormulario()
            tipo_cafe = request.POST.get('tipo_cafe')
            if tipo_cafe:                       
                pedidos = Pedido.objects.filter(tipo_cafe__iexact=tipo_cafe)
                if pedidos:
                    return render(request,"AppGoldenCafe/pedido.html", {'pedidos': pedidos, 'tipo_cafe': tipo_cafe})
                else:
                    mensaje = "El pedido ingresado no existe."
                    return render(request, "AppGoldenCafe/pedido.html", {'mensaje': mensaje, 'form': miFormulario})
            else:
                mensaje = "Por favor, ingresa un pedido para buscar."
                return render(request, "AppGoldenCafe/pedido.html", {'mensaje': mensaje, 'form': miFormulario})
        else:
            miFormulario = pedidoFormulario()
            return render(request, "AppGoldenCafe/pedido.html", {'form': miFormulario})
               
    else:                                                   
        miFormulario = pedidoFormulario()                  
        return render(request, "AppGoldenCafe/pedido.html", {'pedidos': pedidos, 'form': miFormulario})



def sucursal(request):
    sucursales = Sucursal.objects.all()
    miFormulario = sucursalFormulario()
    if request.method == "POST":
        
        if 'agregar_sucursal' in request.POST:
            miFormulario = sucursalFormulario(request.POST)  
            if miFormulario.is_valid():
                sucursal = Sucursal(barrio=miFormulario.cleaned_data['barrio'], id_sucursal=miFormulario.cleaned_data['id_sucursal']) 
                sucursal.save()                             
                return redirect('sucursales')                 
            else:
                return render(request, "AppGoldenCafe/sucursal.html", {'form': miFormulario})
            
        elif 'buscar_sucursal' in request.POST:
            miFormulario = sucursalFormulario()
            barrio = request.POST.get('barrio')
            if barrio:                       
                sucursales = Sucursal.objects.filter(barrio__iexact=barrio)
                if sucursales:
                    return render(request,"AppGoldenCafe/sucursal.html", {'sucursales': sucursales, 'barrio': barrio})
                else:
                    mensaje = "La sucursal ingresada no existe."
                    return render(request, "AppGoldenCafe/sucursal.html", {'mensaje': mensaje, 'form': miFormulario})
            else:
                mensaje = "Por favor, ingresa un barrio pedido para buscar la sucursal."
                return render(request, "AppGoldenCafe/sucursal.html", {'mensaje': mensaje, 'form': miFormulario})
        else:
            miFormulario = sucursalFormulario()
            return render(request, "AppGoldenCafe/sucursal.html", {'form': miFormulario})
               
    else:                                                   
        miFormulario = sucursalFormulario()                  
        return render(request, "AppGoldenCafe/sucursal.html", {'sucursales': sucursales, 'form': miFormulario})




"""
 -- FUNCIONES EN DESUSO TRAS LOS CAMBIOS:

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
        return render(req, "AppGoldenCafe/cliente.html", {'clientes': clientes, 'nombre': nombre}) 
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

"""
