class novaclasse():
	__idade = 2
	nome="novonome"
	def __init__(self):
		print("construtor")
	def __del__(self):
		print("destrutor")
	def alteranome(self):
		print("funcao altera nome")
	def getidade(self):
		return(self.__idade)
	def setidade(self,novaidade):
		self.__idade = novaidade


objeto = novaclasse()
print(objeto.nome)
print(objeto.alteranome())
objeto.nome = "33"
print(objeto.nome)
#print(objeto.__idade)		# acusa como se a variavel nao existisse, pois esta protegida "__"

print(objeto.getidade())
objeto.setidade(42)
print(objeto.getidade())
