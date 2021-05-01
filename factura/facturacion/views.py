from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from django.urls import reverse
from .models import Cliente, ComprobanteGeneral, CampoAdicional, Pagos, Producto
from .forms import ClienteForm, CampoAdicionalForm, PagosForm, ClienteForm2
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from bootstrap_modal_forms.generic import BSModalCreateView


# Create your views here.

def inicio(request):
    return render(request, 'index.html', {})


class ClienteCreateView(BSModalCreateView):
    template_name = 'Cliente.html'
    form_class = ClienteForm2
    success_message = 'Success: Cliente creado con exito'
    success_url = reverse_lazy('factura')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            print("Ver esto",request.POST)
            action = request.POST['action']
            print(action)
        except Exception as e:
            data['error'] = str(e)
            print("Error", str(e))
        return JsonResponse(data, safe=False)

@login_required
def factura(request):
    emisor = ComprobanteGeneral.objects.all().first()

    return render(request, 'factura.html', {'emisor':emisor})


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