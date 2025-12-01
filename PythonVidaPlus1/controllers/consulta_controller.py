


from PythonVidaPlus1.models.consulta import Consulta

class ConsultaController:
    def criar_consulta(self, paciente: str, profissional: str, data: str, motivo: str) -> Consulta:
        return Consulta(paciente, profissional, data, motivo)

    def validar(self, consulta: Consulta) -> bool:
        return all([consulta.paciente, consulta.profissional, consulta.data, consulta.motivo])
