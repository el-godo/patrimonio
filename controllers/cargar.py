
@auth.requires(auth.has_membership('Administrador') or auth.has_membership('Usuario'))
def cargar_dependencia():

    formulario = SQLFORM(db.dependencias)
    

    if formulario.process().accepted:
        redirect(URL(c='nreg',f='nreg'))
    elif formulario.errors:
        response.flash='El formulario tiene errores'
    else:
        response.flash = 'Debe completar el formulario'
    return dict(formulario=formulario)


@auth.requires(auth.has_membership('Administrador') or auth.has_membership('Usuario'))
def cargar_marca():

    formulario = SQLFORM(db.marcas)
    

    if formulario.process().accepted:
        redirect(URL(c='nreg',f='nreg'))
    elif formulario.errors:
        response.flash='El formulario tiene errores'
    else:
        response.flash = 'Debe completar el formulario'
    return dict(formulario=formulario)


@auth.requires(auth.has_membership('Administrador') or auth.has_membership('Usuario'))
def cargar_tipo():

    formulario = SQLFORM(db.tipos)
    

    if formulario.process().accepted:
        redirect(URL(c='nreg',f='nreg'))
    elif formulario.errors:
        response.flash='El formulario tiene errores'
    else:
        response.flash = 'Debe completar el formulario'

    return dict(formulario=formulario)




def sin_autorizacion():
  return dict()