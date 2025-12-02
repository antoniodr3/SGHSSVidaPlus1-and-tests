


class IntegracaoExterna:
    def __init__(self, sistema: str, tipo: str, endpoint: str):
        self.sistema = sistema      # Ex: "Laboratório XYZ"
        self.tipo = tipo            # Ex: "laboratorio", "convenio", "api"
        self.endpoint = endpoint    # URL ou identificador de integração
        self.status = "desconectado"

    def conectar(self):
        self.status = "conectado"

    def desconectar(self):
        self.status = "desconectado"

    def validar(self) -> bool:
        return bool(self.sistema and self.tipo and self.endpoint)
