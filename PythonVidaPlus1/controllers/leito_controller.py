


from PythonVidaPlus1.models.leito import Leito

class LeitoController:
    def criar_leito(self, id_: str, tipo: str) -> Leito:
        return Leito(id_, tipo)

    def ocupar_leito(self, leito: Leito):
        leito.ocupar()
        return leito

    def liberar_leito(self, leito: Leito):
        leito.liberar()
        return leito

    def validar(self, leito: Leito) -> bool:
        return leito.validar()
