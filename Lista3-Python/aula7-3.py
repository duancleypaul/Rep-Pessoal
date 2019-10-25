# Exemplo de uso de classes e SUPER
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

class Cube(Square):
    def surface_area(self):
        face_area = super(Square, self).area()
        return face_area * 6

    def volume(self):
        face_area = super(Square, self).area()
        return face_area * self.length

square = Square(4)
print(square.area())
cube = Cube(3)
print(cube.surface_area())
print(cube.volume())

# Output:
# 16
# 54
# 27
"""
# Manipulacao pessoal do codigo do Andre

class Usuario:
	def __init__(self, nome):
		self.nome = nome

class UsuarioPF(Usuario):
        def __init__(self, nome, cpf):
#                super.__init__(self, nome)	 formato usado pelo Andre
		super.__init__(nome)
		self.cpf = cpf

class UsuarioPJ(Usuario):
	def __init__(self, nome, cnpj):
		super.__init__(self, nome)
		self.cnpj = cnpj

class Conta:
	def __init__(self, saldo, cliente):
		self.saldo = saldo
		self.cliente = cliente
	def saque(valor):
		self.saldo -= valor
		return self.saldo
	def deposito(valor):
		self.saldo += valor
		return self.saldo

class ContaCorrente(Conta):
	def __init__(self, saldo, cliente):
	super.__init__(self, saldo, cliente)

class ContaPoupanca(Conta):
	def __init__(self, saldo, cliente):
		super.__init__(self, saldo, cliente)


user1 = UsuarioPF("Duan Cleypaul","055.798.064-00")		#Duan 05579806400
user2 = UsuarioPF("Lais Cleypaul","145.743.867-46")		#Lais 14574386746
user3 = UsuarioPF("Paulo Ferreira","678.717.984-72")		#Pai  67871798472
user4 = UsuarioPF("Clea Correia","565.014.124-04")		#Mae  56501412404



print(user1.nome, user1.cpf)
print(user2.nome, user1.cpf)
print(user3.nome, user1.cpf)
print(user4.nome, user1.cpf)
print("---")
print()
"""

# Exemplos, aula7-3
'''
class MyClass2:
	idade=0

	def function(self):
		print("This is a message inside MyClass2.")

class MyClass3(MyClass2):
	var2 = "blah2"

	def function2(self):
		print("This is a message inside MyClass3.")

obj = MyClass3()
print(obj.idade)
print(obj.function())
'''

# Tentativa Duan

class ClientControl:
	typeClient = "PF"
	if typeClient == "PF"
		cpf = "000.000.000-00"
	if typeClient == "PJ"
		cnpj = "00.000.000/0001-00"

class BankAccount(ClientControl):
	accountType = "cc"
	__saldo = 0
	def sacar(self,valor):
		self.__saldo -= valor
		if saldo < 0:
			print("Voce esta usando o cheque especial. Saldo atual:",self.__saldo)
		else:
			print("Saldo atual:",self.__saldo)
	def deposita(self,valor):
		self.__saldo += valor
		print("Deposito no valor de",valor,"efetuado com sucesso. Saldo atual:",self.__saldo)

"""

# Versao do Andre, soh a class Usuario que esta modificada (sem def __init__)
"""
class Usuario:
	nome = ""

class UsuarioPF(Usuario):
	def __init__(self, nome, cpf):
		super.__init__(self, nome)
		self.cpf = cpf

class UsuarioPJ(Usuario):
	def __init__(self, nome, cnpj):
		super.__init__(self, nome)
		self.cnpj = cnpj

class Conta:
	def __init__(self, saldo, cliente):
		self.saldo = saldo
		self.cliente = cliente
	def saque(valor):
		self.saldo -= valor
		return self.saldo
	def deposito(valor):
		self.saldo += valor
		return self.saldo

class ContaCorrente(Conta):
	def __init__(self, saldo, cliente):
		super.__init__(self, saldo, cliente)

class ContaPoupanca(Conta):
	def __init__(self, saldo, cliente):
		super.__init__(self, saldo, cliente)

user = Usuario()
user.nome="Duan"
print(user.nome)
"""
