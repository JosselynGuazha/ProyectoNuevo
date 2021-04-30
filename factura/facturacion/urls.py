from django.urls import path 
from .views import  *
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', inicio, name= "Inicio"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name="logout"),
    path('crearCliente/', crearCliente, name= "crearCliente"),
    path('buscarCliente/', buscarCliente, name= "buscarCliente"),
    path('modificarCliente/<int:id>', modificarCliente, name= "modificarCliente"),
    path('campoAdicional/', crear_campoAdicional, name= "campoAdicional"),
    path('buscarDetalle/', buscarDetalle, name= "buscarDetalle"),
    path('formaPago/', crear_formaPago, name= "formaPago"),
    path('factura/', factura, name= "factura"),
    path('clienteCrear/', clienteCrear.as_view(), name= "clienteCrear"),
    
]

    
    