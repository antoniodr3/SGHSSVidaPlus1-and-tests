


import datetime

class Governanca:
    def __init__(self):
        self.backups = []
        self.atualizacoes = []
        self.suporte = []

    def registrar_backup(self, descricao: str):
        self.backups.append({"descricao": descricao, "data": datetime.datetime.now().isoformat()})

    def registrar_atualizacao(self, descricao: str):
        self.atualizacoes.append({"descricao": descricao, "data": datetime.datetime.now().isoformat()})

    def registrar_suporte(self, descricao: str):
        self.suporte.append({"descricao": descricao, "data": datetime.datetime.now().isoformat()})

    def listar_backups(self):
        return self.backups

    def listar_atualizacoes(self):
        return self.atualizacoes

    def listar_suporte(self):
        return self.suporte

    def validar(self) -> bool:
        return isinstance(self.backups, list) and isinstance(self.atualizacoes, list) and isinstance(self.suporte, list)
