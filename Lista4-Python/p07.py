def prime(limit):
	if limit <=1:
		print("Limit must be greater than 1")
	elif limit == 2:
		primos = [2]
		print(primos)
		return primos
	elif limit == 3:
		primos = [2,3]
		print([2,3])
		return primos
	else:
		primos = [2,3]
		lista = list(range(4,limit+1))
		for i in lista:
			for j in range(2,i//2 +1):
				if i%j==0:
					break
				else:
					if i not in primos and j==len(range(2,i//2 +1)):
						primos.append(i)
		return primos


print(prime(100))		# testando a funcao
