


class RelatorioFinanceiro:
    def __init__(self):
        self.entradas = []
        self.saidas = []

    def adicionar_entrada(self, valor):
        self.entradas.append(valor)

    def adicionar_saida(self, valor):
        self.saidas.append(valor)

    def calcular_saldo(self):
        return sum(self.entradas) - sum(self.saidas)

    def validar(self):
        return True  # simples, sempre válido
