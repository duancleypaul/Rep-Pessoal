import sys
lista_in = list(open(sys.argv[1]))

def tail(lista, size=10):
    for i in range(len(lista)-size,len(lista)):
#        print(lista[i].replace('\n',''))
        print(lista[i].rstrip('\n'))
tail(lista_in)

# Implementação do comando Unix "tail"
# tail nomeDoArquivo: imprime as ultimas 10 linhas de nomeDoArquivo

# exemplo de uso: tail teste.txt

# Implementar o comando Unix "grep". 
# Este comando utiliza 2 argumentos:a string and a file as arguments and prints 
# all lines in the file which contain the specified string.
