


from PythonVidaPlus1.models.exame import Exame

class ExameController:
    def criar_exame(self, paciente: str, solicitante: str, tipo: str) -> Exame:
        return Exame(paciente, solicitante, tipo)

    def validar(self, exame: Exame) -> bool:
        return all([exame.paciente, exame.solicitante, exame.tipo])
