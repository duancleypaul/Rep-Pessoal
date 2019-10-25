def showNumbers(limit):
	lista = list(range(limit+1))
	for i in lista:
		if i%2 == 0:
			print(i,"EVEN")
		else:
			print(i,"ODD")

# showNumbers(10)	# testando a funcao
