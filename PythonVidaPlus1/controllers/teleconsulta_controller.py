


from PythonVidaPlus1.models.teleconsulta import Teleconsulta

class TeleconsultaController:
    def criar_teleconsulta(self, paciente, profissional, data: str, motivo: str, link: str, prescricao=None) -> Teleconsulta:
        return Teleconsulta(paciente, profissional, data, motivo, link, prescricao)

    def validar(self, teleconsulta: Teleconsulta) -> bool:
        return teleconsulta.validar()
