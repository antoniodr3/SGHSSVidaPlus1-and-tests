


from PythonVidaPlus1.models.paciente import Paciente

class PacienteController:
    def criar_paciente(self, id_, nome, idade, genero, contato):
        return Paciente(id_, nome, idade, genero, contato)

    def validar(self, paciente: Paciente):
        return paciente.validar()
