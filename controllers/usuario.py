
#--------------------------------------------------------------------

#Funciones para cambiar el widget de buscar
def search_form(self,url): 
    form = FORM('',
INPUT(_name='keywords',_value=request.get_vars.keywords, 
               _style='width:200px;', 
               _id='keywords'), 


         INPUT(_type='submit',_value=T('Search')), 
         INPUT(_type='submit',_value=T('Clear'),

         _onclick="jQuery('#keywords').val('');"), 
         _method="GET",_action=url) 

    return form 


def search_query(tableid,search_text,fields): 
    words= search_text.split(' ') if search_text else [] 
    query=tableid<0#empty query 
    for field in fields: 
        new_query=tableid>0 
        for word in words: 
            new_query=new_query&field.contains(word) 
        query=query|new_query 
    return query

#Fin de las funciones

#------------------------------------------------------------------


def privilegio(row):
        btn = A(I(_class='glyphicon glyphicon-wrench'), 
                    ' Otorgar privilegios de acceso',
                    _href=URL(c='usuario', f='privilegio1', args=[row.id]),
                    _class='btn btn-danger')
        return btn


@auth.requires_membership('Administrador')
def usuario():
	#--Oculto campos
    db.auth_user.id.readable = False
    db.auth_user.email.readable = False

    grid = SQLFORM.grid(db.auth_user,search_widget=search_form,user_signature=False,searchable=True,deletable=False,
        editable=True,details=False,selectable=None,
        create=True,
        csv=False,maxtextlength=100,links=[lambda r: privilegio(r)],
        )
    if grid.element('input', _type='submit'):
        grid.element('input', _type='submit')['_class'] = 'btn btn-primary'
    return dict(grid=grid)

@auth.requires_membership('Administrador')
def privilegio1():
	#--Oculto campos
    db.auth_membership.id.readable = False
    #db.auth_user.email.readable = False

    grid = SQLFORM.grid(db.auth_membership,search_widget=search_form,user_signature=False,searchable=True,deletable=False,
        editable=True,details=False,selectable=None,
        create=True,
        csv=False,maxtextlength=100,
        )
    if grid.element('input', _type='submit'):
        grid.element('input', _type='submit')['_class'] = 'btn btn-primary'
    return dict(grid=grid)


def sin_autorizacion():
  return dict()