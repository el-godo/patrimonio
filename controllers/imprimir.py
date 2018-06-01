

def imprimir2():
	#atrapo el id
	atrapa=request.args[0]
	#atrapo el nombre de la dependencia

	ndepe=request.args[1]

	#consulto por el id de la dependencia y filtro los inactivos
	#query=db((db.carga.dependencia==atrapa)&(db.carga.estado!="Inactivo")).select(orderby="carga.tipo DESC")

	query=db((db.carga.dependencia==atrapa)&(db.carga.estado!="Inactivo")).select()
	settipo=db(db.tipos).select()
	setmarca=db(db.marcas).select()
	l1=[]
	l2=[]
	
	for x in query:
		
		l1.append(x.tipo)

	t=0	

	ax=''	
	l1.sort()#ordeno la lista

	for xi in l1:
		t=0

		if ax == xi:
			t=t+1
			
		else:
			ax=xi
			l2.append(xi)

	cl2=len(l2)		
		


	
	return dict(query=query,ndepe=ndepe,atrapa=atrapa,l1=l1,l2=l2,cl2=cl2,settipo=settipo,setmarca=setmarca)	
