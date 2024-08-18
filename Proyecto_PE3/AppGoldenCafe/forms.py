from django import forms

class clienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=40)

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=20)