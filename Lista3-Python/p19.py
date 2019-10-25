import sys

# recebendo arquivo como argumento na execucao do programa
# e transformando-o em lista
lista = list(open(sys.argv[1]))

# percorrendo cada elemento da lista (total 4)
for line in lista:
    str = ""
    # percorrendo cada elemento de cada um dos 4 elementos d lista
    for i in line:
        str = i + str   #salva em str os caracteres em ordem reversa
    print(str.replace('\n',''))    # removendo \n das strings (substitui "\n" por "")
