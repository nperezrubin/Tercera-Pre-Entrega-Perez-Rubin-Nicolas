from django import forms
from AppGoldenCafe.models import Cliente


class clienteFormulario(forms.forms.Form):
    nombre = forms.CharField(max_length=30)
    email = forms.EmailField()

class pedidoFormulario(forms.Form):
    tipo_cafe = forms.CharField(max_length=30)
    unidades = forms.IntegerField()

class sucursalFormulario(forms.Form):
    barrio = forms.CharField(max_length=30)
    id_sucursal = forms.IntegerField()


