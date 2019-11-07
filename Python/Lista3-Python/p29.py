def enumerate(lista):
	return [(lista.index(i),i) for i in lista]

''' Testando a funcao
lista = ["a","b","c"]
print(enumerate(lista))
[print(index,value) for index, value in enumerate(["a","b","c"])]
'''
