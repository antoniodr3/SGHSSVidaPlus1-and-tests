


from PythonVidaPlus1.models.prontuario import Prontuario

class ProntuarioController:
    def criar_prontuario(self, paciente):
        return Prontuario(paciente)

    def adicionar_registro(self, prontuario: Prontuario, registro):
        prontuario.adicionar_registro(registro)
        return prontuario

    def validar(self, prontuario: Prontuario):
        return prontuario.validar()
