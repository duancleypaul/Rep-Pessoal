def unique(lista):
	novaLista = []
	for i in lista:
		if i not in novaLista:
			novaLista.append(i)
	return novaLista

''' testando funcao
lista1 = [1,2,1,3,2,5]
lista2 = ["hello","hi","hello","hello","ola","falai","falai"]
print(unique(lista1))
print(unique(lista2))
'''
