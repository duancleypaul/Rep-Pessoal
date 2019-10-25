def somaTudo(lista):
        if type(lista[0])==int or type(lista[0])==float:
                resultSoma = sum(lista);
        else:
                resultSoma = lista[0]
                for i in range(1,len(lista)):
                        resultSoma += lista[i]
        return resultSoma

#print(somaTudo([1,2,3]))
#print(somaTudo(["hello","world","comeqta"]))
