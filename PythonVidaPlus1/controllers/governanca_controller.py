


from PythonVidaPlus1.models.governanca import Governanca

class GovernancaController:
    def __init__(self):
        self.governanca = Governanca()

    def registrar_backup(self, descricao: str):
        self.governanca.registrar_backup(descricao)

    def registrar_atualizacao(self, descricao: str):
        self.governanca.registrar_atualizacao(descricao)

    def registrar_suporte(self, descricao: str):
        self.governanca.registrar_suporte(descricao)

    def listar_backups(self):
        return self.governanca.listar_backups()

    def listar_atualizacoes(self):
        return self.governanca.listar_atualizacoes()

    def listar_suporte(self):
        return self.governanca.listar_suporte()

    def validar(self) -> bool:
        return self.governanca.validar()
