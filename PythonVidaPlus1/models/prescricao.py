


class Prescricao:
    def __init__(self, medicamento: str, dosagem: str, frequencia: str, validade: str, profissional: str):
        self.medicamento = medicamento
        self.dosagem = dosagem
        self.frequencia = frequencia
        self.validade = validade
        self.profissional = profissional

    def resumo(self) -> str:
        return f"{self.medicamento} — {self.dosagem}, {self.frequencia} (Validade: {self.validade}) Prescrito por {self.profissional}"

    def validar(self) -> bool:
        return all([self.medicamento, self.dosagem, self.frequencia, self.validade, self.profissional])
