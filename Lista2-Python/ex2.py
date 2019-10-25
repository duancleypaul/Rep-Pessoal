def podeDoarSangue(idade, peso, sono):
	if idade >= 16 and idade <= 69:
		if peso > 50:
			if sono >= 6:
				print("Voce esta' apto a doar sangue!")
			else:
				print("Voce dormiu menos de 6h. Nao pode doar sangue.")
		else:
			print("Voce pesa menos de 50kg. Nao pode doar sangue.")
	else:
		if idade<16:
			print("Voce tem menos de 16 anos. Nao pode doar sangue.")
		else:
			print("Voce tem mais de 69 anos. Nao pode doar sangue.")


idade = int(input("Insira a sua idade: "))
peso = float(input("Insira o seu peso em kg (use ponto para separar decimais): "))
sono = float(input("Quantas hrs de sono voce dormiu nas ultimas 24h? (use ponto para separar decimais): "))

podeDoarSangue(idade,peso,sono)
