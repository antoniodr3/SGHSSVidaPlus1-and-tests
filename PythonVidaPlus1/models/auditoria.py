


import datetime

class Auditoria:
    def __init__(self):
        self.logs = []

    def registrar(self, usuario: str, acao: str):
        timestamp = datetime.datetime.now().isoformat()
        self.logs.append({"usuario": usuario, "acao": acao, "timestamp": timestamp})

    def listar_logs(self):
        return self.logs

    def validar(self) -> bool:
        return isinstance(self.logs, list)
