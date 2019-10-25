def sumMult35(limit):
	lista = list(range(0,limit+1))
	soma = 0
	for i in lista:
		if i%3==0 or i%5==0:
			soma += i
	print(soma)
	return soma

#sumMult35(20)		# testando funcao
