


from PythonVidaPlus1.models.agendamento import Agendamento

class AgendamentoController:
    def criar_agendamento(self, paciente, profissional, consulta):
        return Agendamento(paciente, profissional, consulta)

    def validar(self, agendamento: Agendamento):
        return agendamento.validar()
