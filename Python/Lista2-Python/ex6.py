a = int(input("Insira um numero inteiro entre 1 e 12: "))
while not type(a) == int:
	print("O numero inserido nao eh do tipo inteiro.")
	a = int(input("Insira um numero inteiro entre 1 e 12: "))

if a < 1 or a > 12:
	print("Nao existe mes com este numero.")
else:
	print("Obrigado!")

