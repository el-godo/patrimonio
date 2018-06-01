

def consulta():

    form=SQLFORM.factory(         
        Field('serie',requires=([IS_NOT_EMPTY(),IS_UPPER()] ) ) )
    if form.process().accepted:
            response.flash = 'formulario aceptado'
            redirect(URL(c='nreg',f='consulta1',args=[form.vars.serie]))
           
    elif form.errors:
            response.flash = 'Complete el formulario'
    

           
    
    
    return dict(form=form)
def consulta1():
    miset   =0
    atrapa = request.args[0]
    consulta = db.carga.serie==atrapa
    miset = db(consulta)
    registros = miset.select()
    a=0
    
    a=miset.count()
    if a > 0:
        response.flash = 'Este equipo  ya se encuentra  registrado' 
        
    else:
        
   
        response.flash = 'El equipo  no esta registrado' 
        redirect(URL(c='nreg',f='generar', args=[atrapa]))     


    
      
   # else:
        
        
        #redirect(URL(c='nreg',f='generar', args=[atrapa]))    

    
    #onsulta = (db.carga.serie==a)
   
    




    #a = miset.count() 
    #if a == 0:
         #redirect(URL(c='nreg',f='generar', args=[atrapa]))
       
       
        
   # else:
          #response.flash = 'El equipo ya esta registrado'
       

       

    
    



    return dict( atrapa=atrapa,consulta=consulta,miset=miset,registros=registros,a=a  )

def nreg():
    captura=request.args[0]
    

    
    form = SQLFORM(db.carga)
                                
    if form.process(session=None,formname='prueba').accepted:

            redirect(URL(c='nreg',f='pregunta'))
            response.flash = 'Formulario aceptado'

      
            
    elif form.errors:
            response.flash='El formulario tiene errores'
    else:
            response.flash = 'Debe completar el formulario'
    
            
   
        
            
            
            
        

    
         
                
    return dict(form=form,captura=captura)    

        












def g_serie():

    
    

    #serie=uuid.uuid4()
    #UUID('26fd2706-8baf-433b-82eb-8c7fada847dc')

    return dict()#serie=serie,uuid=uuid) 
def generar():

    import random
    
    serie=[]
    nserie=serie2=serie0=""
    #creo un contador
    c=1
    comp=d=""
    #creo tuplas que contengan los valores q va a tomar el numero de serie 
    a=("1","2","3","4","5","6","7","8","9")
    b=("A","B","C","D","E","F","G","H","I","J","K","L","N","M","O","P","Q","R","S","T","U","V","W","X","Y","Z")
    
    
    
    #genero un numero se serie de 10 digitos  
    while ((c<=2)): 
       
        d=random.choice(b)
        serie.append(d)

        d=random.choice(a)
        serie.append(d)

        d=random.choice(b)
        serie.append(d)

        d=random.choice(a)
        serie.append(d)
        d=random.choice(a)
        serie.append(d)

        c=c+1
    #paso los elementos de la lista a string y los almaceno en una variable 
    for x in serie:
        serie0=serie0+x

    #nserie = " ".join(serie) 
    serie2="12011201"   


    # comparo que el numero generado com la base de datos para asegurar que no se repita
    if db(db.carga.serie==serie0).select():
        comp="el numero de serie ya existe  la base de datos"
    else :
        comp=nserie
        db.carga.serie.default=serie0
        #redirect(URL('nreg', args=[comp]))
    #poner un valor por defecto a un campo del formulario
    
    db.carga.serie.default=request.args[0]    


    form = SQLFORM(db.carga)
                                
    if form.process(session=None,formname='prueba').accepted:

            redirect(URL(c='nreg',f='pregunta'))
            response.flash = 'Formulario aceptado'

      
            
    elif form.errors:
            response.flash='El formulario tiene errores'
    else:
            response.flash = 'Debe completar el formulario'    











        




    return dict(form=form,a=a,b=b,c=c,d=d,x=x,serie=serie,nserie=nserie,serie2=serie2,serie0=serie0,comp=comp,
        )



def pregunta():


    return dict()		




