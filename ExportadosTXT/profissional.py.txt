


class Profissional:
    def __init__(self, id_: str, nome: str, registro: str, especialidade: str, cargo: str):
        self.id_ = id_
        self.nome = nome
        self.registro = registro
        self.especialidade = especialidade
        self.cargo = cargo

    def assinatura(self) -> str:
        return f"{self.nome} ({self.cargo}, {self.especialidade}) - {self.registro}"
