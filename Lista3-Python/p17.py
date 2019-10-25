def extsort(lista):
    # Versao mais curta
    return lista.sort(key=lambda x: x.split(".")[1])

    """ Versao mais longa
	# Separando nome do arquivo de sua extensao
	# Depois salvando cada dupla (nome e extensao) em uma lista de listas

    i=0
	while(i<len(lista)):
		lista[i]=lista[i].split('.')
		i+=1
	# usando funcao lambda para especificar funcao sort() somente na extensao
	lista.sort(key=lambda x:x[1])
	i=0
	strSep = "."
	while(i<len(lista)):
		lista[i]=strSep.join(lista[i])
		i+=1
	return lista
    """
    


''' testando a funcao curta
lista = ['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']
extsort(lista)
print(lista)
'''
