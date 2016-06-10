def prob_5(n, m):
	lista=[0, 0, 0]
	lista[0]=(n[1]*m[2]-n[2]*m[1])
	lista[1]=(n[0]*m[2]-n[2]*m[0])*-1
	lista[2]=(n[0]*m[1]-n[1]*m[0])
	return(lista)