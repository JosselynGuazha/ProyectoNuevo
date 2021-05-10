
function getData(data) {

    $('input[name="identificador"]').val(data.identificacion);
    $('input[name="razonSocial"]').val(data.razonSocial);
    $('input[name="direccion"]').val(data.direccion);

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
          <td> <a href="#" type="button" class="btn btn-danger btn-xs"><i class="fas fa-trash-alt"></i></a> </td>
        </tr>`;
        $("#cuerpoTabla").append(tr)
    }

}

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

$(function () {
    $('.btnBuscarCliente').on('click', function () {
        $('input[name="action"]').val('buscar');
    });

    $('.btnAddCliente').on('click', function () {
        $('input[name="action"]').val('addCliente');
        $('#formCrearCliente')[0].reset();
        $('#crearCliente').modal('show');
    });

    $('.btnAddFormaPago').on('click', function () {
        $('#crearPago').modal('show');
    });

    $('.btnModificarCliente').on('click', function () {
        $('#modificarCliente').modal('show');
        
        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:8000/modificarClienteModal/1',
            success: function (data) {
                console.log('Modificando');
                console.log(data);
                $('#modificarCliente').modal('hide');
                cargarFormularioCliente(data);
            },
            error: function (data) {
                console.log('An error occurred.');
                console.log(data);
            },
        });
    });


    $('#formCrearCliente').on('submit', function (e) {
        e.preventDefault();
        //var parameters = $(this).serializeArray();
        //var parameters = new FormData(this);
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

    $('#formModificarCliente').on('submit', function (e) {
        e.preventDefault();
        //var parameters = $(this).serializeArray();
        //var parameters = new FormData(this);
        var frm = $('#formModificarCliente');
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
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



    
    $('#formCrearPago').on('submit', function (e) {
        e.preventDefault();
        //var parameters = $(this).serializeArray();
        //var parameters = new FormData(this);
        var frm = $('#formCrearPago');
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            success: function (data) {
                console.log('Submission was successful.');
                console.log(data);
                $('#crearPago').modal('hide');
                getData(data);
            },
            error: function (data) {
                console.log('An error occurred.');
                console.log(data);
            },
        });
    });

});



