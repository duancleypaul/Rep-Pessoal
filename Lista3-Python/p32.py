import sys
# versao generalizada do arquivo p31.py
def parse_csv(arquivo, delimitador, comentario):
        lista = list(open(arquivo))
        temp = []
        [temp.append(lista[i].rstrip('\n')) for i in range(0,len(lista)) if not lista[i][0]=='#']
        temp = [temp[i].split(delimitador) for i in range(0,len(temp))]
        return temp

#testando a funcao
arquivo = sys.argv[1]
print(parse_csv(arquivo,'!','#'))

