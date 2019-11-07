import sys

lista_in = list(open(sys.argv[1]))
str_in = sys.argv[2]
print("")   # só pra imprimir mais organizado
for i in lista_in:
    if str_in in i:
        ind = lista_in.index(i)
        print(lista_in[ind].rstrip('\n'))
#        print(lista_in[ind].replace('\n',''))
        
print("")   # só pra imprimir mais organizado

