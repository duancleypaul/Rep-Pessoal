def cumulative_sum(lista):
	if type(lista[0]) == int or type(lista[0]) == float:
		cumul = []
		soma_parcial = 0
		for i in range(0,len(lista)):
			soma_parcial+=lista[i]
			cumul.append(soma_parcial)
		return cumul
	elif type(lista[0]) == str:
		cumul = []
		soma_parcial = ""
		for i in range(0,len(lista)):
			soma_parcial+=lista[i]
			cumul.append(soma_parcial)
		return cumul
	else:
		print("Esta funcao soh reconhece listas com elementos do tipo str, int ou float.")


''' Testando a funcao
lista1 = [1,2,3,4,5]
lista2 = ["hello","world","como","eh","que","ta"]
print(cumulative_sum(lista1))
print(cumulative_sum(lista2))
'''
