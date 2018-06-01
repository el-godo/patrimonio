
def consulta():

    depe=grid=a=x=c=d=b=""

  
        
        
        
    if request.get_vars['depe']:
        depe = request.get_vars['depe']

    a=db.dependencias.nombre.like('%'+depe+'%')
    if a !='':
        
        grid=SQLFORM.grid(a, csv=False,
            create=False,
            searchable=False,
             editable=False,
             deletable=False,
            details=False,
            selectable=None, links=[lambda r: editar_expediente(r),lambda r: editar_btn(r)])


            
        
        
    return dict(depe=depe,a=a ,grid=grid,x=x,b=b,c=c,d=d)    

   
    
    #agregar boton al grid
#creando el boton    


def editar_expediente(row):
        btn = A(I(_class='icon-thumbs-up'),
                    ' Imprimir ',
                    _href=URL(c='imprimir', f='imprimir2', args=[row.id,row.nombre]),
                    _class='btn btn-primary')
        return btn

#creando el boton    
def editar_btn(row):
        btn = A(I(_class='icon-thumbs-up'),
                    ' Editar',
                    _href=URL(c='consulta', f='editar', args=[row.id,row.nombre]),
                    _class='btn btn-primary')
        return btn
 



def editar():
    grid=''
    fields=[db.carga.dependencia,db.carga.tipo,db.carga.marca,db.carga.modelo,db.carga.serie]
        

    
    atrapa=request.args[0]
    query=(db.carga.dependencia==atrapa)
    grid=SQLFORM.grid(query, csv=False,
            create=False,
            searchable=False,
             editable=True,
             deletable=False,
            details=True,
            user_signature=False
           ,fields=fields)
   
    


    return dict(atrapa=atrapa,query=query,grid=grid)




    


       
    
        





        
    
    
    
                        
           

    

   
       

        
    
            
           

    
            









    
   


   

  
def menu():
    return dict()

 





@auth.requires(auth.has_membership('Administrador') or auth.has_membership('Usuario'))
def consulta1():
    
   
    sn= ""
    
    

    
    
    if request.get_vars['sn']:
            sn = request.get_vars['sn']

        
    fields=[db.carga.dependencia,db.carga.tipo,db.carga.marca,db.carga.modelo,db.carga.serie]  
    form=""

    

  

        

    






    if sn!="":

      
       

        form = SQLFORM.grid((db.carga.serie.upper().like('%'+sn+'%')),#|db.carga.dependencia.like('%'+depe+'%'),
            csv=False,
            create=False,
            searchable=False,
             editable=True,
             deletable=False,
            details=True,
            selectable=None,
               
            fields=fields)


            
    
    
    return dict(form=form,sn=sn)


@auth.requires(auth.has_membership('Administrador') or auth.has_membership('Usuario'))
def consulta2():
    sn=""
    depen=""
    form=""
    query=""
    x=""
    dep=""
    depno=""
    #if request.get_vars['depe']:
            #sn = request.get_vars['depe']
    #if depe!="":t
    depen=db.carga.estado
    #friltro los equivos inactivos para no visualizarlos
    #depe=db(depen)
    #dep=depe.estado!="Inactivo".select()
    for depe in db(db.carga.estado!='Inactivo').select():
        print depe.estado



    
    



    return dict(depen=depen,dep=dep,depe=depe,sn=sn,form=form,query=query,x=x)

