


from PythonVidaPlus1.models.medicamento import Medicamento

class MedicamentoController:
    def criar_medicamento(self, id_: str, nome: str, quantidade: int, preco_unitario: float) -> Medicamento:
        return Medicamento(id_, nome, quantidade, preco_unitario)

    def adicionar_estoque(self, medicamento: Medicamento, qtd: int):
        medicamento.adicionar(qtd)
        return medicamento

    def retirar_estoque(self, medicamento: Medicamento, qtd: int):
        return medicamento.retirar(qtd)

    def validar(self, medicamento: Medicamento) -> bool:
        return medicamento.validar()
