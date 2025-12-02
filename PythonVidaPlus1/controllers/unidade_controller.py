


from PythonVidaPlus1.models.unidade_hospitalar import UnidadeHospitalar

class UnidadeController:
    def criar_unidade(self, id_: str, nome: str, endereco: str) -> UnidadeHospitalar:
        return UnidadeHospitalar(id_, nome, endereco)

    def adicionar_leito(self, unidade: UnidadeHospitalar, leito):
        unidade.adicionar_leito(leito)
        return unidade

    def adicionar_internacao(self, unidade: UnidadeHospitalar, internacao):
        unidade.adicionar_internacao(internacao)
        return unidade

    def validar(self, unidade: UnidadeHospitalar) -> bool:
        return unidade.validar()
