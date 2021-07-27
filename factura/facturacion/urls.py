from django.urls import path 
from .views import  *
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', inicio, name= "Inicio"),
    path('crearCliente/', crearCliente, name= "crearCliente"),
    path('buscarCliente/', buscarCliente, name= "buscarCliente"),
    path('modificarCliente/<int:id>', modificarCliente, name= "modificarCliente"),
    path('campoAdicional/', crear_campoAdicional, name= "campoAdicional"),
    path('buscarDetalle/', buscarDetalle, name= "buscarDetalle"),
    path('formaPago/', crear_formaPago, name= "formaPago"),
    path('factura/', factura, name="factura"),
    path('busquedaCliente', busquedaCliente, name= "busquedaCliente"),
    path('crearClienteModal', crearClienteModal, name= "crearClienteModal"),
    path('modificarClienteModal/<int:id>', modificarClienteModal, name= "modificarClienteModal"),
    path('formaPago', crearFormaPagoModal, name= "formaPago"),
    path('busquedaProductoModal', busquedaProductoModal, name= "busquedaProductoModal"),
    
]

    
    