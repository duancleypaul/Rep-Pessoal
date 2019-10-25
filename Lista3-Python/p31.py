import sys

def parse_csv(arquivo):
	lista = list(open(arquivo))
	temp = []
	[temp.append(lista[i].rstrip('\n')) for i in range(0,len(lista))]
	temp = [temp[i].split(',') for i in range(0,len(temp))]
	return temp

''' testando a funcao
arquivo = sys.argv[1]
print(parse_csv(arquivo))
'''
