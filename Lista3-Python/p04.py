def product(lista):
	produto = 1
	for i in range(0,len(lista)):
		produto = produto*lista[i]
	return produto

# print("O produto da lista eh",product([1,2,3,4]))
