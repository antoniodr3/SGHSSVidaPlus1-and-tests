


from PythonVidaPlus1.models.leito import Leito

class LeitoController:
    def criar_leito(self, id_):
        return Leito(id_)

    def ocupar(self, leito: Leito):
        leito.ocupar()
        return leito

    def liberar(self, leito: Leito):
        leito.liberar()
        return leito

    def validar(self, leito: Leito):
        return leito.validar()
