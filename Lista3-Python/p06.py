def reverse(lista):
	lista_temp = []
	for i in range(len(lista)-1,-1,-1):
		lista_temp.append(lista[i])
	return lista_temp

''' linhas de teste
lista1 = [1,2,3,4,5]
print(lista1)
lista2 = ["um","dois","tres"]
print(lista2)

print(reverse(lista1))
print("")
print(reverse(lista2))
'''
