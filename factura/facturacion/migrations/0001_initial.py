# Generated by Django 3.2 on 2021-05-04 15:43

from django.db import migrations, models
import django.db.models.deletion
import facturacion.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CampoAdicional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razonSocial', models.CharField(max_length=100, verbose_name='Apellidos y Nombres/Razón Social')),
                ('tipoIdentificacion', models.CharField(choices=[('01', 'CEDULA'), ('RUC', 'RUC'), ('PASAPORTE', 'PASAPORTE'), ('IDENTIFICACION DEL EXTERIOR', 'IDENTIFICACION DEL EXTERIOR')], default='CEDULA', max_length=50, verbose_name='Tipo Identificacón')),
                ('identificacion', models.CharField(max_length=50, unique=True, verbose_name='Identificacón')),
                ('tipoCliente', models.CharField(choices=[('CLIENTE', 'CLIENTE'), ('SUJETO RETENIDO', 'SUJETO RETENIDO'), ('DESTINATARIO', 'DESTINATARIO')], default='CLIENTE', max_length=50, verbose_name='Tipo Cliente')),
                ('direccion', models.TextField(verbose_name='Dirección')),
                ('telefocnoConvencional', models.CharField(max_length=50, verbose_name='Teléfono Convencional')),
                ('extension', models.CharField(max_length=50, verbose_name='Extensión')),
                ('telefonoCelular', models.CharField(max_length=50, verbose_name='Teléfono Celular')),
                ('correoElectronico', models.EmailField(max_length=50, verbose_name='Correo Electronico')),
            ],
        ),
        migrations.CreateModel(
            name='ComprobantePendiente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ambiente', models.CharField(choices=[('1', 'PRUEBA'), ('2', 'PRODUCCION')], default='1', max_length=1, verbose_name='Ambiente')),
                ('codDoc', models.CharField(choices=[('01', 'Factura'), ('04', 'Nota Credito'), ('05', 'Nota Debito'), ('06', 'Guia Remision'), ('07', 'Guia de Retencion')], default='01', max_length=2, verbose_name='Código Documento')),
                ('establecimiento', models.CharField(max_length=100, verbose_name='Establecimiento')),
                ('fechaEmision', models.DateField(verbose_name='Fecha Emisión')),
                ('ptoEmision', models.CharField(max_length=100, verbose_name='Pto. Emisión')),
                ('ruc', models.CharField(max_length=50, verbose_name='RUC')),
                ('secuencial', models.CharField(max_length=100, verbose_name='Secuencial')),
                ('tipoEmision', models.CharField(max_length=100, verbose_name='Tipo Emisión')),
                ('clavAcc', models.CharField(max_length=50, verbose_name='Clave Acc')),
            ],
        ),
        migrations.CreateModel(
            name='ConfigAplicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='uploads/')),
                ('dirAutorizados', models.CharField(max_length=100, verbose_name='Dirección Autorizados')),
                ('dirFirma', models.CharField(max_length=100, verbose_name='Dirección Firma')),
                ('dirLogo', models.CharField(max_length=100, verbose_name='Dirección Logo')),
                ('passFirma', models.CharField(max_length=50, verbose_name='Password')),
            ],
        ),
        migrations.CreateModel(
            name='ConfigCorreo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correoAsunto', models.CharField(max_length=50, verbose_name='Correo Asunto')),
                ('correoHost', models.CharField(max_length=50, verbose_name='Correo Host')),
                ('correoPass', models.CharField(max_length=50, verbose_name='Correo Password')),
                ('correoPort', models.CharField(max_length=50, verbose_name='Correo Port')),
                ('correoRemitente', models.CharField(max_length=50, verbose_name='Correo Remitente')),
                ('sslHabilitado', models.BooleanField(default=False, verbose_name='SSL Habilitado')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleAdicional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleProforma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, verbose_name='Código')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('precioUnitario', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio Unitario')),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Descuento')),
                ('precioTotalSinImpuesto', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio Total Sin Impuesto')),
            ],
        ),
        migrations.CreateModel(
            name='Impuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baseImponible', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Base Imponible')),
                ('codigo', models.CharField(max_length=50, verbose_name='Código Impuesto')),
                ('codigoPorcentaje', models.CharField(max_length=50, verbose_name='Código Porcentaje')),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Tarifa')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
            ],
        ),
        migrations.CreateModel(
            name='ImpuestoComprobanteRetencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baseImponible', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Base Imponible')),
                ('codDocSustento', models.CharField(max_length=50, verbose_name='Código Doc. sustento')),
                ('codigo', models.CharField(max_length=50, verbose_name='Código')),
                ('codigoRetencion', models.CharField(max_length=50, verbose_name='Código Retención')),
                ('fechaEmisionDocSustento', models.DateField(verbose_name='Fecha Emisión Doc. Sustento')),
                ('numDocSustento', models.IntegerField(verbose_name='Número Doc. Sustento')),
                ('porcentajeRetener', models.IntegerField(verbose_name='Porcentaje Retener')),
                ('valorRetenido', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor Retenido')),
            ],
        ),
        migrations.CreateModel(
            name='Motivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon', models.CharField(max_length=100, verbose_name='Razón')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
            ],
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formaPago', models.CharField(choices=[('SIN UTILIZACION DEL SISTEMA FINANCIERA', '01-SIN UTILIZACIÓN DEL SISTEMA FINANCIERO'), ('COMPESACION DE DEUDAS', '15-COMPESACIÓN DE DEUDAS'), ('TARJETA DE DEBIDO', '16-TARJETA DE DEBITO'), ('DINERO ELECTRONICO', '17-DINERO ELECTRONICO'), ('TARJETA PREPAGO', '18-TARJETA PREPAGO'), ('TARJETA DE CREDITO', '19-TARJETA DE CREDITO'), ('OTROS CON UTILIZACIÓN DEL SISTEMA FINANCIERO', '20-OTROS CON UTILIZACIÓN DEL SISTEMA FINANCIERO'), ('ENDOSO DE TITULOS', '21-ENDOSO DE TITULOS')], default='SIN_UTILIZACION_FINANCIERA', max_length=50, verbose_name='Forma de Pago')),
                ('total', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Total')),
                ('plazo', models.CharField(max_length=50, verbose_name='Plazo')),
                ('unidadTiempo', models.CharField(choices=[('NINGUNA', 'Ninguna'), ('DIAS', 'Días'), ('MESES', 'Meses'), ('AÑOS', 'Años')], default='NINGUNA', max_length=50, verbose_name='Unidad Tiempo')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoPrincipal', models.CharField(max_length=50, verbose_name='Código Principal')),
                ('codigoAuxiliar', models.CharField(max_length=50, verbose_name='Código Auxiliar')),
                ('tipoProducto', models.CharField(choices=[('BIEN', 'BIEN'), ('SERVICIO', 'SERVICIO')], default='BIEN', max_length=10, verbose_name='Tipo Producto')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('precioUnitario', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio Unitario')),
                ('iva', models.CharField(choices=[('0', '0%'), ('2', 'GRAVA IVA'), ('6', 'NO OBJETO DE IMPUESTO'), ('7', 'EXENTO DE IVA')], default='0', max_length=1, verbose_name='IVA')),
                ('ice', models.CharField(max_length=50, verbose_name='ICE')),
                ('irbpnr', models.CharField(choices=[('', 'Selecione...'), ('5001', 'BOTELLAS PLASTICAS NO RETORNABLES')], default='', max_length=10, verbose_name='IRBPNR')),
            ],
        ),
        migrations.CreateModel(
            name='TotalImpuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baseImponible', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Base Imponible')),
                ('codigo', models.CharField(max_length=50, verbose_name='Código')),
                ('codigoPorcentaje', models.CharField(max_length=50, verbose_name='Código Porcentaje')),
                ('descuentoAdicional', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Descuento Adicional')),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Tarifa')),
            ],
        ),
        migrations.CreateModel(
            name='Proforma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dirLogo', models.CharField(default=facturacion.models.asignarLogo, max_length=100, verbose_name='Dirección Logo')),
                ('dirProformas', models.CharField(max_length=100, verbose_name='Dirección Proformas')),
                ('tipoEmision', models.CharField(max_length=100, verbose_name='Tipo Emision')),
                ('razonSocial', models.CharField(max_length=100, verbose_name='Razón Social')),
                ('nombreComercial', models.CharField(max_length=100, verbose_name='Nombre Comercial')),
                ('ruc', models.CharField(max_length=13, verbose_name='RUC')),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('dirMatriz', models.CharField(max_length=100, verbose_name='Dirección Matriz')),
                ('dirEstablecimiento', models.CharField(max_length=50, verbose_name='Dirección Establecimiento')),
                ('fechaEmision', models.DateField(verbose_name='Fecha Emisión')),
                ('razonSocialComprador', models.CharField(max_length=100, verbose_name='Razon Social Comprador')),
                ('identificacionComprador', models.CharField(max_length=50, verbose_name='Identificación Comprador')),
                ('direccionComprador', models.TextField(max_length=100, verbose_name='Dirección Comprador')),
                ('subTotal12', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='SUB Total 12%')),
                ('subTotal0', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='SUB Total')),
                ('subTotalSinImpuesto', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='SUB Total Sin Impuesto')),
                ('iva', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='IVA')),
                ('totalDescuento', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Descuento')),
                ('importeTotal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Importe Total')),
                ('configCorreo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='facturacion.configcorreo', verbose_name='Configuración Correo')),
                ('detalles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.detalleproforma', verbose_name='Detalles')),
                ('infoAdicional', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='facturacion.campoadicional', verbose_name='Campo Adicional')),
            ],
        ),
        migrations.CreateModel(
            name='procesarComprobantePendiente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comprobantePendiente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='facturacion.comprobantependiente', verbose_name='Comprobante Pendiente')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleNotaCredito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('codigoAdicional', models.CharField(max_length=50, verbose_name='Código Adicional')),
                ('codigoInterno', models.CharField(max_length=50, verbose_name='Código Interno')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Descuento')),
                ('precioTotalSinImpuesto', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio Total Sin Impuesto')),
                ('precioUnitario', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio Unitario')),
                ('detallesAdicionales', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.detalleadicional', verbose_name='Detalle Adicional')),
                ('impuestos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.impuesto', verbose_name='Impuesto')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleLiquidacionCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('codigoAuxiliar', models.CharField(max_length=50, verbose_name='Código Auxiliar')),
                ('codigoPrincipal', models.CharField(max_length=50, verbose_name='Código Principal')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Descuento')),
                ('precioTotalSinImpuesto', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio total Sin Impuesto')),
                ('precioUnitario', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio Unitario')),
                ('detalleAdicional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.detalleadicional', verbose_name='Detalle Adicional')),
                ('impuestos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.impuesto', verbose_name='Impuesto')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleGuiaRemision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cantidad')),
                ('codigoAdicional', models.CharField(max_length=50, verbose_name='Código Adicional')),
                ('codigoInterno', models.CharField(max_length=50, verbose_name='Código Interno')),
                ('detallesAdicionales', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='facturacion.detalleadicional', verbose_name='Detalles Adicionales')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('codigoAuxiliar', models.CharField(max_length=50, verbose_name='Código Auxiliar')),
                ('codigoPrincipal', models.CharField(max_length=50, verbose_name='Código Principal')),
                ('descripcion', models.TextField(max_length=50, verbose_name='Descripción')),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Descuento')),
                ('precioTotalSinImpuesto', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio Total Impuesto')),
                ('precioUnitario', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio Unitario')),
                ('detalleAdicional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Campo_Adicional', to='facturacion.detalleadicional', verbose_name='Detalle Adicional')),
                ('impuestos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.impuesto', verbose_name='Impuesto')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.producto', verbose_name='Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Destinatario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codDocSustento', models.CharField(max_length=50, verbose_name='Código Documento Sustento')),
                ('codEstabDestino', models.CharField(max_length=50, verbose_name='Código Estado Destino')),
                ('dirDestinatario', models.TextField(verbose_name='Dirección Destinatario')),
                ('docAduaneroUnico', models.CharField(max_length=50, verbose_name='Documento Aduanero Unico')),
                ('fechaEmisionDocSustento', models.DateField(verbose_name='Fecha Emision Documento Sustento ')),
                ('identificacionDestinatario', models.CharField(max_length=50, verbose_name='Identificación Destinatario')),
                ('motivoTraslado', models.TextField(verbose_name='Motivo Traslado')),
                ('numAutDocSustento', models.IntegerField(verbose_name='Número Aut. Doc. Sustento')),
                ('numDocSustento', models.IntegerField(verbose_name='Número Documento Sustento')),
                ('razonSocialDestinatario', models.CharField(max_length=50, verbose_name='Razón Social Destinatario')),
                ('ruta', models.CharField(max_length=50, verbose_name='Ruta')),
                ('detalles', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='facturacion.detalleguiaremision', verbose_name='Detalles')),
            ],
        ),
        migrations.AddField(
            model_name='comprobantependiente',
            name='configAplicacion',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='facturacion.configaplicacion', verbose_name='Configuración Aplicación'),
        ),
        migrations.AddField(
            model_name='comprobantependiente',
            name='configCorreo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='facturacion.configcorreo', verbose_name='Configuración Correo'),
        ),
        migrations.CreateModel(
            name='ComprobanteGeneral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ambiente', models.CharField(choices=[('1', 'PRUEBA'), ('2', 'PRODUCCION')], default='1', max_length=1, verbose_name='Ambiente')),
                ('claveAcc', models.CharField(max_length=50, verbose_name='Clave Acc')),
                ('codDoc', models.CharField(choices=[('01', 'Factura'), ('04', 'Nota Credito'), ('05', 'Nota Debito'), ('06', 'Guia Remision'), ('07', 'Guia de Retencion')], default='01', max_length=2, verbose_name='Código Documento')),
                ('contribuyenteEspecial', models.CharField(max_length=100, verbose_name='Contribuyente Especial')),
                ('dirEstablecimiento', models.CharField(max_length=100, verbose_name='Direeción Establecimiento')),
                ('dirMatriz', models.CharField(max_length=100, verbose_name='Dirección Matriz')),
                ('establecimiento', models.CharField(max_length=100, verbose_name='Establecimeinto')),
                ('fechaEmision', models.DateField(verbose_name='Fecha Emisión')),
                ('nombreComercial', models.CharField(max_length=100, verbose_name='Nombre Comercial')),
                ('obligadoContabilidad', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='SI', max_length=100, verbose_name='Obligado a LLevar Contabilidad')),
                ('ptoEmision', models.CharField(max_length=100, verbose_name='pto Emisión')),
                ('razonSocial', models.CharField(max_length=100, verbose_name='Razón Social')),
                ('ruc', models.CharField(max_length=13, verbose_name='RUC')),
                ('secuencial', models.CharField(max_length=100, verbose_name='Secuencial')),
                ('tipoDoc', models.CharField(max_length=50, verbose_name='Tipo Documento')),
                ('tipoEmision', models.CharField(max_length=50, verbose_name='Tipo Emisión')),
                ('configAplicacion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='facturacion.configaplicacion', verbose_name='Configuración Aplicación')),
                ('configCorreo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='facturacion.configcorreo', verbose_name='Configuración Correo')),
            ],
        ),
        migrations.CreateModel(
            name='NotaDebito',
            fields=[
                ('comprobantegeneral_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='facturacion.comprobantegeneral')),
                ('codDocModificado', models.CharField(max_length=50, verbose_name='Cod. Documento Modificado')),
                ('fechaEmisionDocSustento', models.DateField(verbose_name='Fecha Emisión Doc. Sustento')),
                ('identificacionComprador', models.CharField(max_length=50, verbose_name='Identificación Comprador')),
                ('numDocModificado', models.IntegerField(verbose_name='Número Doc. Modificado')),
                ('razonSocialComprador', models.CharField(max_length=100, verbose_name='Razón Social Comprado')),
                ('rise', models.CharField(max_length=50, verbose_name='RISE')),
                ('tipoIdentificacionComprador', models.CharField(max_length=50, verbose_name='Tipo Identificación Comprador')),
                ('totalSinImpuestos', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Identificación Comprador')),
                ('valorTotal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor Total')),
                ('impuestos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.impuesto', verbose_name='Impuesto')),
                ('infoAdicional', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='facturacion.campoadicional', verbose_name='Campo Adicional')),
                ('motivos', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='facturacion.motivo', verbose_name='Motivos')),
                ('pagos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.pagos', verbose_name='Pagos')),
            ],
            bases=('facturacion.comprobantegeneral',),
        ),
        migrations.CreateModel(
            name='NotaCredito',
            fields=[
                ('comprobantegeneral_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='facturacion.comprobantegeneral')),
                ('codDocModificado', models.CharField(max_length=50, verbose_name='Código Doc. Modificado')),
                ('fechaEmisionDocSustento', models.DateField(verbose_name='Fecha Emisión Doc. Sustento')),
                ('identificacionComprador', models.CharField(max_length=50, verbose_name='Identificación Comprador')),
                ('moneda', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Moneda')),
                ('motivo', models.CharField(max_length=100, verbose_name='Motivo')),
                ('numDocModificado', models.IntegerField(verbose_name='Número Doc. Modificado')),
                ('razonSocialComprador', models.CharField(max_length=100, verbose_name='Razón Social Comprador')),
                ('rise', models.CharField(max_length=50, verbose_name='RISE')),
                ('tipoIdentificacionComprador', models.CharField(max_length=50, verbose_name='Tipo Identificación Comprador')),
                ('totalSinImpuestos', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Sin Impuesto')),
                ('valorModificacion', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor Modificación')),
                ('detalles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.detallenotacredito', verbose_name='Detalles')),
                ('infoAdicional', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='facturacion.campoadicional', verbose_name='Campo Adicional')),
                ('totalConImpuesto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='facturacion.totalimpuesto', verbose_name='Total Con Impuesto')),
            ],
            bases=('facturacion.comprobantegeneral',),
        ),
        migrations.CreateModel(
            name='LiquidacionCompra',
            fields=[
                ('comprobantegeneral_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='facturacion.comprobantegeneral')),
                ('direccionProveedor', models.CharField(max_length=100, verbose_name='Dirección Proveedor')),
                ('identificacionProveedor', models.CharField(max_length=50, verbose_name='Identificación Proveedor')),
                ('importeTotal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Importe Total')),
                ('moneda', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Moneda')),
                ('razonSocialProveedor', models.CharField(max_length=100, verbose_name='Razón Social Proveedor')),
                ('tipoIdentificacionProveedor', models.CharField(max_length=100, verbose_name='Tipo de identificación Proveedor')),
                ('totalDescuento', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total con Descuento')),
                ('totalSinImpuestos', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total sin Impuesto')),
                ('detalles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.detalleproforma', verbose_name='Detalles')),
                ('infoAdicional', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='facturacion.campoadicional', verbose_name='Campo Adicional')),
                ('pagos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.pagos', verbose_name='Pagos')),
                ('totalConImpuesto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='facturacion.totalimpuesto', verbose_name='Total Con Impuesto')),
            ],
            bases=('facturacion.comprobantegeneral',),
        ),
        migrations.CreateModel(
            name='GuiaRemision',
            fields=[
                ('comprobantegeneral_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='facturacion.comprobantegeneral')),
                ('dirPartida', models.TextField(verbose_name='Direccion Partida')),
                ('fechaFinTransporte', models.DateField(verbose_name='Fecha Fin Transporte')),
                ('fechaIniTransporte', models.DateField(max_length=50, verbose_name='Fecha Inicio Transporte')),
                ('placa', models.CharField(max_length=10, verbose_name='Placa')),
                ('razonSocialTransportista', models.CharField(max_length=50, verbose_name='Razón Social Transportista')),
                ('rise', models.CharField(max_length=50, verbose_name='RISE')),
                ('rucTransportista', models.CharField(max_length=50, verbose_name='RUC Transportista')),
                ('tipoIdentificacionTransportista', models.CharField(max_length=50, verbose_name='Tipo Identificación Trnasportista')),
                ('destinatarios', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='facturacion.destinatario', verbose_name='Destinatarios')),
                ('infoAdicional', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='facturacion.campoadicional', verbose_name='Campo Adicional')),
            ],
            bases=('facturacion.comprobantegeneral',),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('comprobantegeneral_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='facturacion.comprobantegeneral')),
                ('identificacionComprador', models.CharField(max_length=100, verbose_name='Identificación del Comprador')),
                ('importeTotal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Importe Total')),
                ('moneda', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Moneda')),
                ('propina', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Propina')),
                ('razonSocialComprador', models.CharField(max_length=100, verbose_name='Razón social Comprador')),
                ('tipoIdentificacionComprador', models.CharField(choices=[('04', 'RUC'), ('05', 'Cedula'), ('06', 'Pasaporte'), ('07', 'Consumidor final'), ('08', 'ID Exterior'), ('09', 'Placa')], default='07', max_length=50, verbose_name='Tipo Identificación Comprador')),
                ('totalDescuento', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Descuento')),
                ('totalSinImpuestos', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Sin Impuesto')),
                ('direccionComprador', models.TextField(verbose_name='Dirección Comprador')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.cliente', verbose_name='Cliente')),
                ('detalles', models.ManyToManyField(to='facturacion.DetalleFactura', verbose_name='Detalles')),
                ('infoAdicional', models.ManyToManyField(related_name='campoAdicional', to='facturacion.CampoAdicional', verbose_name='Campo Adicional')),
                ('pagos', models.ManyToManyField(to='facturacion.Pagos', verbose_name='Pagos')),
                ('totalConImpuesto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='facturacion.totalimpuesto', verbose_name='Total con Impuesto')),
            ],
            bases=('facturacion.comprobantegeneral',),
        ),
        migrations.CreateModel(
            name='ComprobanteRetencion',
            fields=[
                ('comprobantegeneral_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='facturacion.comprobantegeneral')),
                ('identificacionSujetoRetenido', models.CharField(max_length=100, verbose_name='Identificación Sujeto Retenido')),
                ('periodoFiscal', models.CharField(max_length=100, verbose_name='Periodo Fiscal')),
                ('razonSocialSujetoRetenido', models.CharField(max_length=100, verbose_name='Razón Social Sujeto Retenido')),
                ('tipoIdentificacionSujetoRetenido', models.CharField(max_length=50, verbose_name='Tipo Idrntificación Sujeto Retenido')),
                ('impuestos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.impuestocomprobanteretencion', verbose_name='Impuestos')),
                ('infoAdicional', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='facturacion.campoadicional', verbose_name='Campo Adicional')),
            ],
            bases=('facturacion.comprobantegeneral',),
        ),
    ]
