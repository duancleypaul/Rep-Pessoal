def zip(l1,l2):
	if len(l1)!=len(l2):
		print("Listas nao possuem o mesmo tamanho")
		return
	else:
		temp = []
		[temp.append([l1[i],l2[i]]) for i in range(0,len(l1))]
		temp = [tuple(temp[j]) for j in range(0,len(temp))]

	return temp

''' Dados para teste da funcao
lista1 = [1,2,3]
lista2 = ["a","b","c"]

print(zip(lista1,lista2))
'''
