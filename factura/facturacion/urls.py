from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.inicio, name= "Inicio"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name="logout"),
    path('crearCliente/', views.crearCliente, name= "crearCliente"),
    path('buscarCliente/', views.buscarCliente, name= "buscarCliente"),
    path('modificarCliente/<int:id>', views.modificarCliente, name= "modificarCliente"),
    path('campoAdicional/', views.crear_campoAdicional, name= "campoAdicional"),
    path('buscarDetalle/', views.buscarDetalle, name= "buscarDetalle"),
    path('formaPago/', views.crear_formaPago, name= "formaPago"),
    path('factura/', views.factura, name= "factura"),
]
    
    