


class Exame:
    def __init__(self, paciente: str, solicitante: str, tipo: str):
        self.paciente = paciente
        self.solicitante = solicitante
        self.tipo = tipo

    def descricao(self) -> str:
        return f"Exame: {self.tipo} para {self.paciente}, solicitado por {self.solicitante}"
