import math

a = int(input("Insira um numero: "))
if a >= 0:
	print("Numero positivo. Sua raiz eh",math.sqrt(a))
else:
	print("Numero negativo. Seu quadrado eh",a*a)
