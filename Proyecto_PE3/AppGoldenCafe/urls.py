from AppGoldenCafe import views
from django.urls import path



urlpatterns = [
    #URL de la pagina principal:
    path('padre/', views.inicio, name='padre'),

    #URLs de las vistas de cada clase:
    path('cliente/', views.cliente, name='cliente'),
    path('pedido/', views.pedido, name='pedido'),
    path('sucursal/', views.sucursal, name='sucursal'),

    #URLs de los formularios para cada clase:
    path('cliente_form_2/', views.cliente_form_2, name='cliente_form_2'),
    path('pedido_form_2/', views.pedido_form_2, name='pedido_form_2'),
    path('sucursal_form_2/', views.sucursal_form_2, name='sucursal_form_2'),

    #URLs de búsqueda:
    path('busquedaCliente/', views.busquedaCliente, name='BusquedaCliente'),
    path('busquedaPedido/', views.busquedaPedido, name='BusquedaPedido'),
    path('busquedaSucursal/', views.busquedaSucursal, name='BusquedaSucursal'),

    path('buscarcliente/', views.buscarcliente),
    path('buscarpedido/', views.buscarpedido),
    path('buscarsucursal/', views.buscarsucursal),
]


   #path('clienteFormulario/', views.clienteFormulario, name='clienteFormulario'),