from django import forms


class clienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=40)

class pedidoFormulario(forms.Form):
    tipo_cafe = forms.CharField(max_length=30)
    unidades = forms.IntegerField()

class sucursalFormulario(forms.Form):
    barrio = forms.CharField(max_length=30)
    id_sucursal = forms.IntegerField()


#class Buscar(forms.Form):
#    nombre = forms.CharField(max_length=20)