class ContaBancaria:
    def __init__(self, nome, saldo=0):
        self.nome = nome
        self.saldo = saldo

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def saque(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser maior que zero.")

    def extrato(self):
        print(f"Extrato bancário de {self.nome}:")
        print(f"Saldo disponível: R${self.saldo}")

# Exemplo de uso do sistema bancário
conta = ContaBancaria("João")

conta.deposito(1000)
conta.saque(500)
conta.extrato()
