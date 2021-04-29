from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cliente, ComprobanteGeneral, CampoAdicional, Pagos, Producto
from .forms import ClienteForm, CampoAdicionalForm, PagosForm
from django.contrib import messages
from django.db.models import Q


# Create your views here.

def inicio(request):
    return render(request, 'index.html', {})

@login_required
def factura(request):
    emisor = ComprobanteGeneral.objects.all().first()
    print("ver este valor", emisor)
    

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
    context = {}
    identificacionGet = request.GET.get("identificacion")
    tipoIdentificacionGet = request.GET.get("tipoIdentificacion")

    if identificacionGet and tipoIdentificacionGet:
        if tipoIdentificacionGet == 'TODOS':
            cliente = Cliente.objects.get(identificacion = identificacionGet)
            cont = Cliente.objects.filter(identificacion = identificacionGet).count()
        else:
            cliente = Cliente.objects.filter(identificacion = identificacionGet, tipoIdentificacion = tipoIdentificacionGet).first()
            cont = Cliente.objects.filter(identificacion = identificacionGet, tipoIdentificacion = tipoIdentificacionGet).count()
        if cont == 0:
            context = {'message' : 'Cliente no existe'}
        else:
            context = {'data' : cliente}
    return render(request, 'buscarCliente.html', context)


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
                return render(request, 'buscarCliente.html', context)

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