from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from .models import Cliente, ComprobanteGeneral, CampoAdicional, Pagos, Producto
from .forms import ClienteForm, CampoAdicionalForm, PagosForm, ClienteForm2
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from bootstrap_modal_forms.generic import BSModalCreateView

from django.views.generic import TemplateView
from django.http import QueryDict

# Create your views here.

def inicio(request):
    return render(request, 'index.html', {})


class FacturaView(TemplateView):
    template_name = 'factura.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'addCliente':
                cli = Cliente()
                cli.razonSocial = request.POST['razonSocial']
                cli.tipoIdentificacion = request.POST['tipoIdentificacion']
                cli.identificacion = request.POST['identificacion']
                cli.tipoCliente = request.POST['tipoCliente']
                cli.direccion = request.POST['direccion']
                cli.telefocnoConvencional = request.POST['telefocnoConvencional']
                cli.extension = request.POST['extension']
                cli.telefonoCelular = request.POST['telefonoCelular']
                cli.correoElectronico = request.POST['correoElectronico']
                cli.save()
                print("Hola", request.POST)
                data = request.POST
            elif action == 'buscar':
                print('Bscando...')
                identificacionGet = request.POST['identificador']
                print("Mira",identificacionGet)
                cliente = Cliente.objects.values().get(identificacion = identificacionGet)
                print(cliente)
                data = QueryDict(cliente)
                print(data)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emisor'] = ComprobanteGeneral.objects.all().first()
        #context['list_url'] = reverse_lazy('factura')
        #context['entity'] = 'Clientes'
        context['form'] = ClienteForm()
        return context
    
    


#class ClienteCreateView(CreateView):
 #   template_name = 'Cliente.html'
  #  form_class = ClienteForm
   # success_message = 'Success: Cliente creado con exito'
    #success_url = reverse_lazy('factura')

#class ClienteCreateView(CreateView):
 #   template_name = 'Cliente.html'
  #  form_class = ClienteForm

#    def post(self, request, *args, **kwargs):
 #       form = ClienteForm(request.POST)
  #      if form.is_valid():
   #         form.save()
    #        return redirect('factura')
     #   else:
      #      form = ClienteForm()
       # return render(request, 'Cliente.html')

#def crearClienteFactura(request):
 #   if request.method == "POST":
  #      form = ClienteForm(request.POST)
   #     if form.is_valid():
    #        form.save()
     #       return redirect('factura')
    #else:
     #   form = ClienteForm()
    #return render(request, 'Cliente.html', {'form': form})
    

#@login_required
#def factura(request):
 #   emisor = ComprobanteGeneral.objects.all().first()

  #  return render(request, 'factura.html', {'emisor':emisor})


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