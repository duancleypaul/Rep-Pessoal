def lensort(lista):
	sortedListLen = lista
	sortedListLen.sort(key=len)
	return sortedListLen

''' testando funcao
lista1 = ['python', 'perl', 'java', 'c', 'haskell', 'ruby']

print(lensort(lista1))
'''
