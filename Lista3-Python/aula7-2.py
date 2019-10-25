class MyClass:
	idade = 0
	def __init__(self, idadeInicial):
		self.idade = idadeInicial

	def __del__(self):
		self.idade=0

	def function(self):
		print("This is a message inside the class.")


class MyClassAux:
	numero = 10

obj = MyClassAux()
print(obj.numero)


myobjectx = MyClass(12)
print(myobjectx.idade)

