import sys
lista_in = list(open(sys.argv[1]))

def head(lista,size=10):
    for i in range(0,size):
#        print(lista[i].replace('\n',''))
         print(lista[i].rstrip('\n'))
head(lista_in)

# Implementação de comando Unix "head" 
# head nomeDoArquivo: imprime as primeiras 10 linhas de nomeDoArquivo

# exemplo de uso: head teste.txt
