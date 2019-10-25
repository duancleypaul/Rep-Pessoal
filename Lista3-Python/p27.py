def even(x): return x%2==0

def filter(fun,lista):
	temp = []
	[temp.append(lista[i]) for i in range(0,len(lista)) if fun(lista[i])]
	return temp

#print(filter(even,range(10)))		# testando funcoes
