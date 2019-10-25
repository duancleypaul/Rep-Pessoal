def group(lista, size):
	listaTemp=[]
	groupedList=[]
	i=0
	while i<len(lista):
		if(len(listaTemp)<size):
			listaTemp.append(lista[i])
			i=i+1
		else:
			groupedList.append(listaTemp)
			listaTemp=[]

	groupedList.append(listaTemp)
	return groupedList

''' exemplo mais enxuto da internet
def group(lista, size):
	return [lista[i:i+size] for i in range(0, len(lista), size)]
'''

''' testando a funcao
lista = [1,2,3,4,5,6,7,8,9,10]
print(group(lista,4))
'''
