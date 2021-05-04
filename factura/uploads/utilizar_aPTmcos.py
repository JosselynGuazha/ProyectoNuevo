if identificacionGet and tipoIdentificacionGet:
        if tipoIdentificacionGet == 'TODOS':
            cont = Cliente.objects.filter(identificacion = identificacionGet).count()
        else:
            cliente = Cliente.objects.filter(identificacion = identificacionGet, tipoIdentificacion = tipoIdentificacionGet).first()
            cont = Cliente.objects.filter(identificacion = identificacionGet, tipoIdentificacion = tipoIdentificacionGet).count()
        if cont == 0:
            context = {'message' : 'Cliente no existe'}
        else:
            context = {'data' : cliente}