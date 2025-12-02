


from PythonVidaPlus1.models.prescricao import Prescricao

class PrescricaoController:
    def criar_prescricao(self, medicamento: str, dosagem: str, frequencia: str, validade: str, profissional: str) -> Prescricao:
        return Prescricao(medicamento, dosagem, frequencia, validade, profissional)

    def validar(self, prescricao: Prescricao) -> bool:
        return prescricao.validar()
