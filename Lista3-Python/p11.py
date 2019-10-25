def dups(lista):
	duplicada = []
	lista.sort()
	for i in range(0,len(lista)-1):
		if lista[i] == lista[i+1] and lista[i] not in duplicada:
			duplicada.append(lista[i])
	return duplicada

''' testando funcao
lista1 = [1,2,2,3,4,5,5,6,7,7,1]
print(dups(lista1))
'''
