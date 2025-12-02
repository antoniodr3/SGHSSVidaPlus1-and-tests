


class UnidadeHospitalar:
    def __init__(self, id_: str, nome: str, endereco: str):
        self.id = id_
        self.nome = nome
        self.endereco = endereco
        self.leitos = []
        self.internacoes = []

    def adicionar_leito(self, leito):
        self.leitos.append(leito)

    def adicionar_internacao(self, internacao):
        self.internacoes.append(internacao)

    def listar_leitos(self):
        return self.leitos

    def listar_internacoes(self):
        return self.internacoes

    def validar(self) -> bool:
        return bool(self.id and self.nome and self.endereco)
