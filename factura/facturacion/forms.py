from django import forms

from .models import Cliente, CampoAdicional, DetalleFactura, Pagos

class ClienteForm(forms.ModelForm):

    class Meta:
        
        model = Cliente
        fields = ('razonSocial', 'tipoIdentificacion', 'identificacion', 'tipoCliente', 'direccion', 'telefocnoConvencional', 'extension','telefonoCelular','correoElectronico')
        widgets = {
            'razonSocial': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoIdentificacion': forms.Select(attrs={'class': 'form-control'}),
            'identificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoCliente': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control','rows':'3'}),
            'telefocnoConvencional': forms.TextInput(attrs={'class': 'form-control'}),
            'extension': forms.TextInput(attrs={'class': 'form-control'}),
            'telefonoCelular': forms.TextInput(attrs={'class': 'form-control'}),
            'correoElectronico': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CampoAdicionalForm(forms.ModelForm):

    class Meta:
        model = CampoAdicional
        fields = ('nombre', 'valor')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PagosForm(forms.ModelForm):

    class Meta:
        model = Pagos
        fields = ('formaPago', 'total', 'plazo', 'unidadTiempo')
        widgets = {
            'formaPago': forms.Select(attrs={'class': 'form-control'}),
            'total': forms.TextInput(attrs={'class': 'form-control'}),
            'plazo': forms.TextInput(attrs={'class': 'form-control'}),
            'unidadTiempo': forms.Select(attrs={'class': 'form-control'}),
        }
