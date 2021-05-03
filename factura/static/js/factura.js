
function getData(data){
    var identificador = $('#identificador');
    $('input[name="identificador"]').val(data.identificacion);
    $('input[name="razonSocial"]').val(data.razonSocial);
    $('input[name="direccion"]').val(data.direccion);
    

}
$(function () {

    $('.btnAddCliente').on('click', function () {
        $('input[name="action"]').val('addCliente');
        $('#crearCliente').modal('show');
    });

    $('form').on('submit', function (e) {
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
        //submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
          //  $('#crearCliente').modal('hide');
            //tblClient.ajax.reload();
            //getData();
            //location.reload();
        //});
    });

});