def cumulative_product(lista):
	if type(lista[0]) == int or type(lista[0]) == float:
		cumul_prod = []
		prod_parcial = 1
		for i in range(0,len(lista)):
			prod_parcial*=lista[i]
			cumul_prod.append(prod_parcial)
		return cumul_prod
	else:
		print("Esta funcao soh reconhece listas com elementos do tipo inteiro.")

''' Testando funcao
lista1 = [1,2,3,4,5]
lista2 = ["hello","world","como","eh","que","ta"]
print(cumulative_product(lista1))
print(cumulative_product(lista2))
'''
