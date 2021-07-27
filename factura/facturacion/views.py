from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from .models import Cliente, ComprobanteGeneral, CampoAdicional, Pagos, Producto, DetalleFactura
from .forms import ClienteForm, CampoAdicionalForm, PagosForm, DetalleFacturaForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from bootstrap_modal_forms.generic import BSModalCreateView
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import TemplateView
from django.http import HttpResponse
import json
#from django.http import QueryDictrequest

# Create your views here.

def inicio(request):
    return render(request, 'index.html', {})


@login_required
@csrf_exempt
def factura(request):
    if request.method == "POST":
        print("Body---> ",request.body)
        body = json.loads(request.body.decode('utf-8'))
        arrayDetalles = body.get("arrayDetalles")
        print("Body---> ", arrayDetalles)
        #decodeData = json.loads(request.body.decode ('utf-8'))
        #print("DATA---> ", decodeData)
        
        for detalle in arrayDetalles:
            print("DETALLE", detalle)
            print(detalle)
            detalleSave = DetalleFacturaForm(detalle)
            detalleSave.save()
    else:
        emisor = ComprobanteGeneral.objects.all().first()
        form = ClienteForm()
        formulario = PagosForm()
        return render(request, 'factura.html', {'emisor': emisor, 'form': form, 'formulario': formulario})


@login_required
def busquedaCliente(request):
    identificacionGet = request.GET.get("identificacion")
    cliente = Cliente.objects.get(identificacion=identificacionGet)
    cliente = cliente_serializable(cliente)
    print(cliente)
    return HttpResponse(json.dumps(cliente), content_type='application/json')


def crearClienteModal(request):
    form = ClienteForm(request.POST)
    if form.is_valid():
        cliente = form.save()
        cliente = cliente_serializable(cliente)
        return HttpResponse(json.dumps(cliente), content_type='application/json')


@login_required
def modificarClienteModal(request, id):    
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save()
            cliente = cliente_serializable(cliente)
            return HttpResponse(json.dumps(cliente), content_type='application/json')
    else:
        cliente = cliente_serializable(cliente)
        print("Form ---- ", cliente)
        return HttpResponse(json.dumps(cliente), content_type='application/json')

def crearFormaPagoModal(request):
    form = PagosForm(request.POST)
    if form.is_valid():
        pago = form.save()
        pago = pago_serializable(pago)
        return HttpResponse(json.dumps(pago), content_type='application/json')

@login_required
def busquedaProductoModal(request):
    codigo = request.GET.get("codProducto")
    if codigo:
        productos = Producto.objects.filter(Q(codigoPrincipal = codigo) | Q(codigoAuxiliar = codigo))
    else: 
        productos = Producto.objects.all()
    productos = [ producto_serializable(producto) for producto in productos]
    return HttpResponse(json.dumps(productos), content_type='application/json')
#AQUI NOS QUEDAMOS.... HACER CON AJAX AL ABRIR MODAL AL para cargar los productos y hacer la buscquueda y caragr en la tabla Detalle Factura


#Form para mantar Data en Forma json
def cliente_serializable(cliente):
    return {
        'id': cliente.id,
        'razonSocial' : cliente.razonSocial,
        'tipoIdentificacion' : cliente.tipoIdentificacion,
        'identificacion' : cliente.identificacion,
        'tipoCliente' : cliente.tipoCliente,
        'direccion': cliente.direccion,
        'telefonoConvencional': cliente.telefonoConvencional,
        'extension': cliente.extension,
        'telefonoCelular': cliente.telefonoCelular,
        'correoElectronico': cliente.correoElectronico
    }

def pago_serializable(pago):
    return {
        'id': pago.id,
        'formaPago' : pago.formaPago,
        'total' : pago.total,
        'plazo' : pago.plazo,
        'unidadTiempo' : pago.unidadTiempo,
    }

def producto_serializable(producto):
    return {
        'id': producto.id,
        'codigoPrincipal' : producto.codigoPrincipal,
        'codigoAuxiliar' : producto.codigoAuxiliar,
        'tipoProducto' : producto.tipoProducto,
        'nombre' : producto.nombre,
        'precioUnitario' : producto.precioUnitario,
        'iva' : producto.iva,
        'ice' : producto.ice,
        'irbpnr' : producto.irbpnr,
    }

@login_required
def crearCliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente guardado con Exito')
            return redirect('crearCliente')
    else:
        form = ClienteForm()
    return render(request, 'crearCliente.html', {'form': form})


@login_required
def buscarCliente(request):
    message=''
    print(request.GET)
    identificacionGet = request.GET.get("identificacion")
    tipoIdentificacionGet = request.GET.get("tipoIdentificacion")
    clientes = Cliente.objects.all().order_by('razonSocial')

    if identificacionGet and tipoIdentificacionGet:
        if tipoIdentificacionGet == 'TODOS':
            clientes = Cliente.objects.filter(identificacion = identificacionGet)
        else:
            clientes = Cliente.objects.filter(identificacion = identificacionGet, tipoIdentificacion = tipoIdentificacionGet)

        if clientes.exists() == False:
            message = 'Cliente no existe'

    paginator = Paginator(clientes, 2)
    page = request.GET.get('page')
    clientes = paginator.get_page(page)

    parametros = request.GET.copy()
    if parametros.get('page') != None:
        del parametros['page']

    return render(request, 'buscarCliente.html', {'clientes': clientes, 'parametros':parametros, 'message':message})


@login_required
def modificarCliente(request, id):    
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
            form = ClienteForm(request.POST, request.FILES, instance=cliente)
            if form.is_valid():
                cliente = form.save()
                cliente.save()
                context = {'data' : cliente}
                messages.success(request, 'Cliente Modificado con Exito')
                return redirect('buscarCliente')

    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'modificarCliente.html', {'form':form})

@login_required
def crear_campoAdicional(request):
    if request.method == "POST":
        formulario = CampoAdicionalForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Campo guardado con Exito')
            return redirect('campoAdicional')
    else:
        formulario = CampoAdicionalForm()
    return render(request, 'campoAdicional.html', {'formulario':formulario })

@login_required
def buscarDetalle(request):
    codigo = request.GET.get("codigo")
    print("Ver este Valor", codigo)
    producto = Producto.objects.filter()
    if codigo:
        producto = Producto.objects.filter(Q(codigoPrincipal = codigo) | Q(codigoAuxiliar = codigo))

    return render(request, 'buscarDetalle.html', {'data': producto})

@login_required
def crear_formaPago(request):
    if request.method == "POST":
        formulario = PagosForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Pago guardado con Exito')
            return redirect('formaPago')
    else:
        formulario = PagosForm()
    return render(request, 'formaPago.html', {'formulario':formulario })