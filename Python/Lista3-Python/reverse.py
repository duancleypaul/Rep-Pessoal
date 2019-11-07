import sys

lista = list(open(sys.argv[1]))
for line in reversed(lista):
    print(line.rstrip())

# este programa não salva a lista revertida
# apenas imprime a lista revertida na tela
# OBS: o uso de SYS permite usar a funcao .argv
# para receber o argumento passado na hora de chamar
# o programa no terminal.
# Dessa forma, ao chamar via terminal 
# "python reverse.py she.txt", tem-se "reverse.py" como 
# sys.argv[0] e "she.txt" como sys.argv[1], etc