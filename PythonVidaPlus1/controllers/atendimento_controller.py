


from PythonVidaPlus1.models.atendimento import Atendimento

class AtendimentoController:
    def criar_atendimento(self, paciente, profissional, consulta=None, exame=None):
        return Atendimento(paciente, profissional, consulta, exame)

    def validar(self, atendimento: Atendimento):
        return atendimento.validar()
