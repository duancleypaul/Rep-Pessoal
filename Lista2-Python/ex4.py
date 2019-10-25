def result(a,b):
	soma = a + b
	if soma > 20:
		result = soma + 8
	else:
		result = soma - 5
	return result

a = int(input("Insira o primeiro numero: "))
b = int(input("Insira o segundo numero: "))

print(result(a,b))

