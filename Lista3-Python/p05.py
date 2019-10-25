import sys
sys.path.append('p04')

from p04 import product
'''
def product(lista):
        produto = 1
        for i in range(0,len(lista)):
                produto = produto*lista[i]
        return produto
'''

def factorial(num):
	if type(num) != int:
		print("Nao eh possivel calcular o fatorial de um numero nao inteiro.")
	if num < 0:
		print("Nao eh possivel calcular o fatorial de um numero negativo.")
	if num == 0:
		fat = 1
	else:
		lista_temp = []
		for i in range(1,num+1):
			lista_temp.append(i)

		fat = product(lista_temp)
	return fat

#n = 4
#print("O fatorial de", n, "eh",factorial(n))

