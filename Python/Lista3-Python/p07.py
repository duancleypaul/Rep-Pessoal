def myMin(lista):
	minVal = lista[0]
	for i in range(0,len(lista)):
		if lista[i] <= minVal:
			minVal = lista[i]
	return minVal

def myMax(lista):
	maxVal = lista[0]
	for i in range(0,len(lista)):
		if lista[i] >= maxVal:
			maxVal = lista[i]
	return maxVal

''' testando funcao
lista1 = [2,7,5,5,5,4,5,2,-1,18,-2]
print("Menor valor da lista:",myMin(lista1))
print("Maior valor da lista: ",myMax(lista1))
'''
