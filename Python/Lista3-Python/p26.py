def square(x):
	if type(x)==int or type(x)==float:
		return x*x

#print(square([1,2,3]))		# testando funcao square

def map(fun, lista):
	return [fun(lista[i]) for i in range(0,len(lista))]

# print(map(square,[1,2,3,4,5]))	# testando funcao map




