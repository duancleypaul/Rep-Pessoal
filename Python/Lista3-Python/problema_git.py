class Cliente:
    def __init__(self, nome, sobrenome, cpf, endereco):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.endereco = endereco
    
    def nomeCompleto(self):
        return self.nome + " " + self.sobrenome
    

class Conta:
    __saldo = 0
    saldoImpresso = __saldo
    def __init__(self, titular, tipoConta, numero):
        self.titular = titular
        self.tipoConta = tipoConta
        self.numero = numero
    
    def saque(self, valor):
        if self.__saldo - valor >= 0: 
            self.__saldo -= valor
            print("> Saque na conta",self.numero,"efetuado com sucesso. Saldo atual: ",self.__saldo)
            return True
        else:
            print("Operação negada!\nVocê não possui saldo suficiente. Saldo atual:",self.__saldo,"\n---")
            return False
    def deposito(self, valor):
        self.__saldo += valor
        print("> Depósito na conta",self.numero,"efetuado com sucesso. Saldo atual: ",self.__saldo,"\n---")
        return True
    def transferencia(self, destino, valor):
        print("--- Solicitação de Transferência ---")
        saqueRealizado = self.saque(valor)
        if saqueRealizado:
            destino.deposito(valor)
            return print("Transferência realizada com sucesso.\n---")
    def extrato(self):
        print("--- Extrato da Conta",self.numero,"---")
        print("Titular:", self.titular.nomeCompleto())
        print("Conta:", self.numero)
        print("Tipo de Conta:", self.tipoConta)
        print("Saldo atual:", self.__saldo)
        return "---"

c1 = Cliente("Duan","Cleypaul","055.798.064-00",
    "Rua Santos Dummont, 532, Casa 5")
duan = Conta(c1,"Conta Corrente","123-4")

print(duan.extrato())

duan.deposito(500)

c2 = Cliente("Lais","Cleypaul","145.743.867-46",
    "Rua Santos Dummont, 532, Casa 5")
lais = Conta(c2,"Conta Corrente","112-3")

print(lais.extrato())

duan.transferencia(lais,300)

print(duan.extrato())
print(lais.extrato())
