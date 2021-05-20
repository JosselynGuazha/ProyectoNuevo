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
    <td><input style="width: 70px"  value="1" type="number" id="cantidad_${data.codigoPrincipal}" onkeyup="actualizarTotal(${data.codigoPrincipal})"/></td>
    <td>${data.codigoPrincipal}</td>
    <td>${data.codigoAuxiliar}</td>
    <td>${data.nombre}</td>
    <td><input style="width: 70px" type="number" value="${data.precioUnitario}" id="precioUnitario_${data.codigoPrincipal}" disabled/></td>
    <td><input style="width: 70px" type="number" value="0" id="descuento_${data.codigoPrincipal}" onkeyup="actualizarTotal(${data.codigoPrincipal})"/></td>
    <td><select name="porcentaje">
    <option value="12" selected>12 %</option>
    <option value="14" >14 %</option>
    </select></td>
    <td><input style="width: 70px" type="number" name="valorTotal" id="total_${data.codigoPrincipal}" value="${total}" disabled/></td>
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
    $('#detalleFactura tbody tr').each(function () {
        console.log("LLegando al EACH");
        var valorTotal = $(this).find('input[name="valorTotal"]').val();
        console.log(valorTotal);
        subTotalSinImpuesto = subTotalSinImpuesto + parseFloat(valorTotal);
        $(`#subTotalSinImpuesto`).val(subTotalSinImpuesto);
        
        // var des = JSON.stringify(fila);
        //alert(des);
    });
}

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
});



