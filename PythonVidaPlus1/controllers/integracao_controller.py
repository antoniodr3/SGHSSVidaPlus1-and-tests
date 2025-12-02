


from PythonVidaPlus1.models.integracao_externa import IntegracaoExterna

class IntegracaoController:
    def criar_integracao(self, sistema: str, tipo: str, endpoint: str) -> IntegracaoExterna:
        return IntegracaoExterna(sistema, tipo, endpoint)

    def conectar(self, integracao: IntegracaoExterna):
        integracao.conectar()
        return integracao

    def desconectar(self, integracao: IntegracaoExterna):
        integracao.desconectar()
        return integracao

    def validar(self, integracao: IntegracaoExterna) -> bool:
        return integracao.validar()
