


class Medicamento:
    def __init__(self, id_: str, nome: str, quantidade: int, preco_unitario: float):
        self.id = id_
        self.nome = nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def adicionar(self, qtd: int):
        self.quantidade += qtd

    def retirar(self, qtd: int):
        if qtd <= self.quantidade:
            self.quantidade -= qtd
            return True
        return False

    def validar(self) -> bool:
        return bool(self.id and self.nome and self.quantidade >= 0 and self.preco_unitario >= 0)
