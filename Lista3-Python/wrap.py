import sys

lista = list(open(sys.argv[1]))
size = int(sys.argv[2])

for i in lista:
    wrapped = i
    # enquanto houver mais que "size" caracteres na string 
    # que esta sendo lida, o loop irá imprimir apenas "size"
    # caracteres e ir atualizando a variavel temporaria "wrapped" 
    while len(wrapped) > size:
        print(wrapped[:size])
        wrapped = wrapped[size:]
    print(wrapped.rstrip('\n'))
#    print(wrapped.replace('\n',''))	# outra forma de fazer a linha acima

