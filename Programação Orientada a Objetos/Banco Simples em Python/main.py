import random


class ContaCorrente:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0


    def depositar(self,valor):
        self.saldo += valor
        print(f'DEPOSITO REALIZADO COM SUCESSO!\n')
        print(f'Você Depositou R${valor:,.2f}')

    def consultar_saldo(self):
        print(f'Seu saldo é de R${self.saldo :,.2f}')


    def sacar(self, valor):

        if valor < self.saldo:
            self.saldo -= valor
            print(f'Você acabou de sacar R${valor:,.2f}')
        else:
            print("Saldo Insuficiente")


    def linha(self):
        print("==================================================")





# programa

conta_wisley = ContaCorrente("wisley", "122.122.212-12")
conta_wisley.linha()
conta_wisley.consultar_saldo()

# depositando um dinheirinho na conta
conta_wisley.linha()
conta_wisley.depositar(10000)

# sacando o nosso dinheirinho na conta
conta_wisley.linha()
conta_wisley.sacar(5000)

conta_wisley.linha()
conta_wisley.consultar_saldo()


