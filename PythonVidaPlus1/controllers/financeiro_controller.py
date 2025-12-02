


from PythonVidaPlus1.models.financeiro import Financeiro

class FinanceiroController:
    def __init__(self):
        self.financeiro = Financeiro()

    def registrar_transacao(self, descricao: str, valor: float):
        self.financeiro.registrar_transacao(descricao, valor)

    def calcular_total(self) -> float:
        return self.financeiro.calcular_total()

    def listar_transacoes(self):
        return self.financeiro.listar_transacoes()

    def validar(self) -> bool:
        return self.financeiro.validar()
