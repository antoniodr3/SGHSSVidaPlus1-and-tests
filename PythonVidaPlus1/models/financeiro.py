


class Financeiro:
    def __init__(self):
        self.transacoes = []

    def registrar_transacao(self, descricao: str, valor: float):
        self.transacoes.append({"descricao": descricao, "valor": valor})

    def calcular_total(self) -> float:
        return sum(t["valor"] for t in self.transacoes)

    def listar_transacoes(self):
        return self.transacoes

    def validar(self) -> bool:
        return isinstance(self.transacoes, list)
