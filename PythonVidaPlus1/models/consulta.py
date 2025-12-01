


class Consulta:
    def __init__(self, paciente: str, profissional: str, data: str, motivo: str):
        self.paciente = paciente
        self.profissional = profissional
        self.data = data
        self.motivo = motivo

    def resumo(self) -> str:
        return f"Consulta de {self.paciente} com {self.profissional} em {self.data} — Motivo: {self.motivo}"

