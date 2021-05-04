
function getData(data) {
    $('input[name="identificador"]').val(data.identificacion);
    $('input[name="razonSocial"]').val(data.razonSocial);
    $('input[name="direccion"]').val(data.direccion);

}

$(function () {

    $('.btnBuscarCliente').on('click', function () {
        $('input[name="action"]').val('buscar');
    });


    $('.btnAddCliente').on('click', function () {
        $('input[name="action"]').val('addCliente');
        $('#formCrearCliente')[0].reset();
        $('#crearCliente').modal('show');
    });


    // $('.btnModificarCliente').on('click', function () {

    //   $('#modificarCliente').modal('show');
    //});


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
                console.log(data);
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
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            success: function (data) {
                console.log('Submission was successful.');
                console.log(data);
                getData(data);
                console.log(data);
            },
            error: function (data) {
                console.log('An error occurred.');
                console.log(data);
            }
        });
    });
});



