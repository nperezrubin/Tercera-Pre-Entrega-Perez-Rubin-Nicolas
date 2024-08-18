from django.shortcuts import render
#from django.http import HttpResponse
from AppGoldenCafe.models import Cliente
from AppGoldenCafe.forms import clienteFormulario

# Create your views here.


def inicio(req):
    return render(req, "appgoldencafe/padre.html")


def cliente(req):
    return render(req, "appgoldencafe/cliente.html")

def pedido(req):
    return render(req, "appgoldencafe/pedido.html")

def sucursal(req):
    return render(req, "appgoldencafe/sucursal.html")



def clienteFormulario(req):
    if req.method == 'POST':
        cliente = Cliente(nombre=req.POST['nombre'], email=req.POST['email'])
        cliente.save()
        return render(req, "AppGoldenCafe/padre.html")
    
    return render(req, "AppGoldenCafe/clienteFormulario.html")


#con django:
def cliente_form_2(request):

      if request.method == "POST":
            miFormulario = clienteFormulario(request.POST) # creamos un objeto formulario con los datos enviados
            print(miFormulario) #para depuracion (opcional)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data #obtenemos los datos limpios y validados
                  cliente = Cliente(nombre=informacion["nombre"], email=informacion["email"]) #creamos un objeto Cliente
                  cliente.save() #Guardamos el cliente en la BBDD
                  return render(request, "AppGoldenCafe/padre.html") #redirigimos a la pagina de inicio
      else:
            miFormulario = clienteFormulario() #creamos un formulario vacio para mostrarlo inicialmente
 
      return render(request, "AppGoldenCafe/cliente_form_2.html", {"miFormulario": miFormulario})
