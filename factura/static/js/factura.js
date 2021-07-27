//Variables generales para las rutas y contador general para las tabla campo adicional
var url_modificar;
var count = 0;


function getData(data) {

    $('input[name="identificacion"]').val(data.identificacion);
    $('input[name="razonSocial"]').val(data.razonSocial);
    $('input[name="direccion"]').val(data.direccion);
    url_modificar = `http://127.0.0.1:8000/modificarClienteModal/${data.id}`

    var campos = [
        'Dirección',
        'Teléfono',
        'Email'
    ]

    var valores = [
        data.direccion,
        data.telefonoCelular,
        data.correoElectronico
    ]

    $("#campoAdicional-table td").remove();
    for (let i = 0; i < valores.length; i++) {
        var tr = `<tr>
          <td>`+ campos[i] + `</td>
          <td>`+ valores[i] + `</td>
          <td> <input type="button" value="Delete" onclick="deleteRow(this)"/> </td>
        </tr>`;
        $("#cuerpoTabla").append(tr)
        count++;
    }

}

function añadirProducto(data) {
    console.log("agrgando....", data);
    var total = data.precioUnitario;
    document.getElementById("bodydetalleFactura").insertRow(-1).innerHTML = `
    <td style="display:none;"><input style="width: 70px" type="hidden" value="${data.id}" name="idProducto"/></td>
    <td><input style="width: 70px" value="1" type="number" id="cantidad_${data.codigoPrincipal}" name="cantidadProducto" onkeyup="actualizarTotal(${data.codigoPrincipal})"/></td>
    <td><input style="width: 70px" name="codigoPrincipalProducto" value="${data.codigoPrincipal}" disabled /></td>
    <td><input style="width: 70px" name="codigoAuxiliarProducto" value="${data.codigoAuxiliar}" disabled /></td>
    <td name="nombreProducto">${data.nombre}</td>
    <td><input style="width: 70px" type="number" value="${data.precioUnitario}" id="precioUnitario_${data.codigoPrincipal}"  name="precioUnitario" disabled/></td>
    <td><input style="width: 70px" type="number" name="totalDescuento" value="0" id="descuento_${data.codigoPrincipal}" onkeyup="actualizarTotal(${data.codigoPrincipal})"/></td>
    <td><input style="width: 70px" value="${data.iva}" name="valorIVA" disabled/></td>
    <td><input style="width: 70px" type="number" value="0.00" name="valorICE" onkeyup="actualizarTotal(${data.codigoPrincipal})"/></td>
    <td><input style="width: 70px" type="number" value="0.00" name="valorIRBPNR" onkeyup="actualizarTotal(${data.codigoPrincipal})"/></td>
    <td><input style="width: 70px" type="number" name="valorTotal" id="total_${data.codigoPrincipal}" value="${total}" disabled/></td>
    <td style="display:none;"><input style="width: 70px" type="hidden" value="${data.ice}" name="ICE"/></td>
    <td style="display:none;"><input style="width: 70px" type="hidden" value="${data.irbpnr}" name="IRBPNR"/></td>
    <td><input type="button" value="Eliminar" onclick="deleteRow(this)"/> </td>`
    calcularValoresTotales();

}


//funcion para el total en Detalle de Factura Tabla
function actualizarTotal(codigoPrincipal) {
    var cantidad = $(`#cantidad_${codigoPrincipal}`).val();
    var precioUnitario = $(`#precioUnitario_${codigoPrincipal}`).val();
    var descuento = $(`#descuento_${codigoPrincipal}`).val();
    var total = $(`#total_${codigoPrincipal}`).val();
    total = (cantidad * precioUnitario) - descuento;
    $(`#total_${codigoPrincipal}`).val(total);
    calcularValoresTotales();
    checkPropina();

}

//funcion para un producto en Detalle de Factura Tabla
function cargarTabla(data) {
    $('#producto tbody').empty();
    var productoAdd;
    for (let producto of data) {
        console.log(producto);
        productoAdd = JSON.stringify(producto);
        document.getElementById("producto-tbody").insertRow(-1).innerHTML = `
    <td>${producto.codigoPrincipal}</td>
    <td>${producto.codigoAuxiliar}</td>
    <td>${producto.nombre}</td>
    <td>${producto.precioUnitario}</td>
    <td><input type="button" value="Añadir" onclick='añadirProducto(${productoAdd});'/> </td>`
    }
}


//funcion para cargar Totales Detalle de Factura
function calcularValoresTotales() {
    var subTotalSinImpuesto = 0;
    var totalDescuento = 0;
    var subTotal12 = 0;
    var subTotal0 = 0;
    var subTotalNoObjetoIVA = 0;
    var subTotalNoExentoIVA = 0;
    var total12 = 0;
    var totalValorICE = 0;
    var totalValorIRBPNR = 0;


    $('#detalleFactura tbody tr').each(function () {
        var valorTotal = $(this).find('input[name="valorTotal"]').val();
        var iva = $(this).find('input[name="valorIVA"]').val();
        var descuento = $(this).find('input[name="totalDescuento"]').val();
        var ice = $(this).find('input[name="ICE"]').val();
        var valorice = $(this).find('input[name="valorICE"]').val();
        var irbpnr = $(this).find('input[name="IRBPNR"]').val();
        var valorirbpnr = $(this).find('input[name="valorIRBPNR"]').val();


        totalDescuento = totalDescuento + parseFloat(descuento);
        subTotalSinImpuesto = subTotalSinImpuesto + parseFloat(valorTotal);
        $(`#totalDescuento`).val(totalDescuento);
        $(`#subTotalSinImpuesto`).val(subTotalSinImpuesto);

        //Comparacion para Valores del iva
        if (iva == "0") subTotal0 = subTotal0 + parseFloat(valorTotal);
        if (iva == "2") subTotal12 = subTotal12 + parseFloat(valorTotal);
        if (iva == "6") subTotalNoObjetoIVA = subTotalNoObjetoIVA + parseFloat(valorTotal);
        if (iva == "7") subTotalNoExentoIVA = subTotalNoExentoIVA + parseFloat(valorTotal);
        $(`#subTotal0`).val(subTotal0);
        $(`#subTotal12`).val(subTotal12);
        $(`#subTotalNoObjetoIVA`).val(subTotalNoObjetoIVA);
        $(`#subTotalNoExentoIVA`).val(subTotalNoExentoIVA);
        //comparacion para valores ICE
        if (ice != 'null') totalValorICE = totalValorICE + parseFloat(valorice);
        $(`#valorICE`).val(totalValorICE);
        //comparacion para valores IRBPNR
        if (irbpnr != 'null') totalValorIRBPNR = totalValorIRBPNR + parseFloat(valorirbpnr);
        $(`#valorIRBPNR`).val(totalValorIRBPNR);

        
    });

    total12 = (subTotal12 + totalValorICE) * 0.12;
    $(`#totalIVA`).val(total12.toFixed(2));

    //Valor TOTAL FINAL
    var total = subTotalSinImpuesto + total12 + totalValorICE + totalValorIRBPNR - totalDescuento;
    $(`#valorTOTAL`).val(total.toFixed(2));

    //propina
    $(`#propina10`).val(0);

}

function checkPropina() {
    var subTotalSinImpuesto = $('input[id="subTotalSinImpuesto"]').val();
    var valorTotal = $('input[id="valorTOTAL"]').val();
    var propina = document.getElementById("checkPropina");
    if (propina.checked == true) {
        var totalPropina = parseFloat(subTotalSinImpuesto) * 0.10;
        $(`#propina10`).val(totalPropina.toFixed(2));
        valorTotal = parseFloat(valorTotal) + totalPropina;
        $(`#valorTOTAL`).val(valorTotal.toFixed(2));
    }else{
        calcularValoresTotales();
    }
};

//funcion para cargar el pago en la tabla
function getPago(data) {
    document.getElementById("formaPago-table").insertRow(-1).innerHTML = `
    <td>${data.formaPago}</td>
    <td>${data.formaPago}</td>
    <td>${data.total}</td>
    <td>${data.plazo}</td>
    <td>${data.unidadTiempo}</td>
    <td> <input type="button" value="Delete" onclick="deleteRow(this)"/> </td>`
}


//Eliminar Fila Campo Adicional
function deleteRow(btn) {
    var row = btn.parentNode.parentNode;
    row.parentNode.removeChild(row);
    count--;
}

//Agregar Fila Campo Adicional
function agregarFila() {
    if (count < 5) {
        document.getElementById("campoAdicional-table").insertRow(-1).innerHTML = '<td><input/></td><td><input/></td><td> <input type="button" value="Delete" onclick="deleteRow(this)"/> </td>';
        count++;
    }
}

//Cargar Formulario Editar Cliente
function cargarFormularioCliente(data) {
    console.log("LLegams a cargarFormularioCliente")
    console.log(data)
    $('input[name="razonSocial"]').val(data.razonSocial);
    $('input[name="tipoIdentificacion"]').val(data.tipoIdentificacion);
    $('input[name="identificacion"]').val(data.identificacion);
    $('input[name="tipoCliente"]').val(data.tipoCliente);
    $('textarea[name="direccion"]').val(data.direccion);
    $('input[name="telefonoConvencional"]').val(data.telefonoConvencional);
    $('input[name="extension"]').val(data.extension);
    $('input[name="telefonoCelular"]').val(data.telefonoCelular);
    $('input[name="correoElectronico"]').val(data.correoElectronico);

};





//Funcion General para los modal
$(function () {

    $('.btnBuscarCliente').on('click', function () {
        $('input[name="action"]').val('buscar');
    });

    //Metodo para abrir Modal 
    $('.btnAddCliente').on('click', function () {
        $('input[name="action"]').val('addCliente');
        $('#formCrearCliente')[0].reset();
        $('#crearCliente').modal('show');
    });

    $('.btnAddFormaPago').on('click', function () {
        $('#formCrearPago')[0].reset();
        $('#crearPago').modal('show');
    });

    $('.btnAddDetalle').on('click', function () {
        $('#addDetalleModal').modal('show');
        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:8000/busquedaProductoModal',
            success: function (json) {
                console.log('Submission was successful.');
                console.log(json);
                cargarTabla(json);
            },
            error: function (data) {
                console.log('An error occurred.');
                console.log(data);
            }
        });
    });

    //Metodo para cargar el Formulario en el Modal
    $('.btnModificarCliente').on('click', function () {
        $('#modificarCliente').modal('show');
        $.ajax({
            type: 'GET',
            url: url_modificar,
            success: function (data) {
                $('#modificarCliente').modal('hide');
                cargarFormularioCliente(data);
            },
            error: function (data) {
                console.log('An error occurred.');

            },
        });
    });

    //Metodo para crear Cliente
    $('#formCrearCliente').on('submit', function (e) {
        e.preventDefault();
        var frm = $('#formCrearCliente');
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            success: function (data) {
                console.log('Submission was successful.');
                console.log(data);
                $('#crearCliente').modal('hide');
                getData(data);
            },
            error: function (data) {
                console.log('An error occurred.');
                console.log(data);
            },
        });
    });

    //Metodo de Modificar Cliente 
    $('#formModificarCliente').on('submit', function (e) {
        e.preventDefault();
        var frm = $('#formModificarCliente');
        $.ajax({
            type: frm.attr('method'),
            url: url_modificar,
            data: frm.serialize(),
            success: function (data) {
                console.log('Submission was successful.');
                console.log(data);
                $('#modificarCliente').modal('hide');
                getData(data);
            },
            error: function (data) {
                console.log('An error occurred.');
                console.log(data);
            },
        });
    });

    //Metodo Buscar Cliente
    $('#formBuscarCliente').on('submit', function (e) {
        e.preventDefault();
        var frm = $('#formBuscarCliente');
        console.log(frm.attr('action'));
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            success: function (json) {
                console.log('Submission was successful.');
                console.log(json);
                getData(json);
            },
            error: function (data) {
                console.log('An error occurred.');
                console.log(data);
            }
        });
    });


    //Metodo para Crear Forma de Pago 
    $('#formCrearPago').on('submit', function (e) {
        e.preventDefault();
        var frm = $('#formCrearPago');
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            success: function (data) {
                console.log('Submission was successful.');
                console.log(data);
                $('#crearPago').modal('hide');
                getPago(data);
            },
            error: function (data) {
                console.log('An error occurred.');
                console.log(data);
            },
        });
    });


    //Metodo Buscar Producto
    $('#formAddDetalle').on('submit', function (e) {
        e.preventDefault();
        var frm = $('#formAddDetalle');
        console.log(frm.attr('action'));
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            success: function (json) {
                console.log('Submission was successful.');
                console.log(json);
                cargarTabla(json);
            },
            error: function (data) {
                console.log('An error occurred.');
                console.log(data);
            }
        });
    });

    //Crear Factura
    $('#guardarFactura').on('click', function (e) {
        e.preventDefault();
        console.log("LLegamos a Factura");
        var arrayDetalles = [];
        $('#detalleFactura tbody tr').each(function () {
            arrayDetalles.push({
                producto: $(this).find('input[name="idProducto"]').val(),
                cantidad: $(this).find('input[name="cantidadProducto"]').val(),
                codigoPrincipal: $(this).find('input[name="codigoPrincipalProducto"]').val(),
                codigoAuxiliar: $(this).find('input[name="codigoAuxiliarProducto"]').val(),
                descuento: $(this).find('input[name="totalDescuento"]').val(),
                detalleAdicional: "1",
                impuestos: "1",
                //detalleAdicional: $(this).find('input[name="nombreProducto"]').val(),
                //impuestos: $(this).find('input[name="nombreProducto"]').val(),
                precioTotalSinImpuesto: $(this).find('input[name="valorTotal"]').val(),
                precioUnitario: $(this).find('input[name="precioUnitario"]').val(),
            });
        });
        console.log("Ver ARRAY",arrayDetalles);
        var data = JSON.stringify(({
            arrayDetalles,
            nombre: 'Josselyn'
        }));
        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:8000/factura/',
            contentType: "application/json",
            data,
            dataType: 'json',
            success: function (data) {
                console.log('¡La factura ha sido guardada con éxito!');
            },
            error: function (data) {
                console.log('An error occurred.');
                console.log(data);
            },
        });
    });
});



