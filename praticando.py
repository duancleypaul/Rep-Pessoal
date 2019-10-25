nomes = ["André", "Daniel", "Cristiano",
"Wana", "Duan", "Harrison",
"Alessandra", "Bruna", "Alexandre",
"Lázaro", "Vitor", "Leonardo",
"Sávio", "Lucas", "Rafael",
"Jéssica", "Letícia", "Gabriel",
"Gabriela", "Felipe", "Muriel"]

def listaSemD(nomes):
	if not type(nomes)==list: return
	
	auxiliar = list()
	for elemento in nomes:
		if not elemento[0].lower() == 'd':
			auxiliar.append(elemento)
	return auxiliar

print(listaSemD(nomes))



'''
sizeLista = int(input("Insira o tamanho da lista: "))

listaUsr = []

for i in range(0,sizeLista):
	listaUsr.append(i)

print(listaUsr)
'''
'''
1- Pedir um valor pro usuario

2- Criar uma lista do tamanho do valor do input
'''
'''
1- Lista com o nome dos 20 alunos

2- Loop para percorrer lista

3- Se o nome comecar com D, nao mostrar

4- fazer dentro de uma funcao
'''
