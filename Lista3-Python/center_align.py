import sys

lista = list(open(sys.argv[1]))

# encontrando a maior linha do arquivo
longest=len(max(lista))

for i in lista:
	# encontrando o centro de cada linha, usando como referencia a mais longa
	centro=int((longest-len(i))/2)
	print((' '*centro+i).rstrip('\n'))


