# A lista não possui p35.py
# testar programa com she.txt
import sys
lista = list(open(sys.argv[1]))
def charFrequency(lista):
    lista_dict = dict()
    mostFrequent = -1
    pair = dict()
    for line in lista:
        
        for char in line:
            if char == " ": continue    # não conta espaços em branco
            char = char.lower()
            if char in lista_dict:
                lista_dict[char] += 1
            else:
                lista_dict[char] = 1
            if lista_dict[char] > mostFrequent: 
                mostFrequent = lista_dict[char]
                pair = {char: mostFrequent}

    # imprimindo dicionário com a frequencia dos caracteres
    print(lista_dict)
    # imprimindo o caracter de maior frequencia
    print("\nMost frequent: ",pair)
    
charFrequency(lista)

