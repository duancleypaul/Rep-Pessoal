def raizes2grau(a,b,c):
	delta = (b**2)-4*a*c
	if a == 0:
		print("A equacao inserida nao eh de segundo grau.")
	else:
		if delta > 0:
			print("A equacao possui duas raizes reais distintas.")
		if delta == 0:
			print("A equacao possui duas raizes reais iguais.")
		if delta < 0:
			print("As raizes da equacao nao sao reais.")

a = int(input("Insira o valor do coeficiente de grau 2: "))
b = int(input("Insira o valor do coeficiente de grau 1: "))
c = int(input("Insira o valor do coeficiente de grau 0: "))

raizes2grau(a,b,c)
