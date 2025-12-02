


class Teleconsulta:
    def __init__(self, paciente, profissional, data: str, motivo: str, link: str, prescricao=None):
        self.paciente = paciente
        self.profissional = profissional
        self.data = data
        self.motivo = motivo
        self.link = link
        self.prescricao = prescricao

    def resumo(self) -> str:
        return f"Teleconsulta de {self.paciente} com {self.profissional} em {self.data} — Motivo: {self.motivo} (Link: {self.link})"

    def validar(self) -> bool:
        return all([self.paciente, self.profissional, self.data, self.motivo, self.link])
