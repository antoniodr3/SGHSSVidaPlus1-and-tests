


class Usuario:
    def __init__(self, id_: str, nome: str, perfil: str):
        self.id = id_
        self.nome = nome
        self.perfil = perfil  # "paciente", "profissional", "admin"

    def validar(self) -> bool:
        return bool(self.id and self.nome and self.perfil)
