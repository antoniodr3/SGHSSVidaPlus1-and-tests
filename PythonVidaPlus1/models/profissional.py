


class Profissional:
    def __init__(self, nome: str, especialidade: str, registro: str):
        self.nome = nome
        self.especialidade = especialidade
        self.registro = registro

    def resumo(self) -> str:
        return f"{self.nome} — {self.especialidade} (Registro: {self.registro})"
