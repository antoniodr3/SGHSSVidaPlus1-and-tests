


from PythonVidaPlus1.models.internacao import Internacao

class InternacaoController:
    def criar_internacao(self, paciente, profissional, leito, data_entrada: str) -> Internacao:
        leito.ocupar()
        return Internacao(paciente, profissional, leito, data_entrada)

    def finalizar_internacao(self, internacao: Internacao, data_alta: str):
        internacao.finalizar(data_alta)
        return internacao

    def validar(self, internacao: Internacao) -> bool:
        return internacao.validar()
