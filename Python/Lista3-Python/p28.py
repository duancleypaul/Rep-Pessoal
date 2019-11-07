def triplets(n):
	if n < 3: return False
	else:
		return [(i,j-i,j) for j in range(2,n) for i in range(1,j//2+1)]

# print(triplets(15))		# testando a funcao

''' Explicando o codigo:
O valor do terceiro elemento, j, eh tomado como base, pois tem-se a referencia
  de que nao pode ultrapassar o valor maximo do argumento 'n'. O loop 'i' ira 
  determinar o valor do primeiro elemento da tupla (i), garantindo que nao 
  repetira tuplas no formato (a,b,c)=(b,a,c).
'''
