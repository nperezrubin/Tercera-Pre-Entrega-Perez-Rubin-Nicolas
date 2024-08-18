from AppGoldenCafe import views
from django.urls import path



urlpatterns = [
    path('padre/', views.inicio, name='padre'),
    path('cliente/', views.cliente, name='cliente'),
    path('pedido/', views.pedido, name='pedido'),
    path('sucursal/', views.sucursal, name='sucursal'),
    path('clienteFormulario/', views.clienteFormulario, name='clienteFormulario'),
    path('cliente_form_2/', views.cliente_form_2, name='cliente_form_2'),
]