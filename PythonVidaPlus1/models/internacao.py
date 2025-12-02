


class Internacao:
    def __init__(self, paciente, profissional, leito, data_entrada: str, data_alta: str = None):
        self.paciente = paciente
        self.profissional = profissional
        self.leito = leito
        self.data_entrada = data_entrada
        self.data_alta = data_alta

    def finalizar(self, data_alta: str):
        self.data_alta = data_alta
        if self.leito:
            self.leito.liberar()

    def validar(self) -> bool:
        return all([self.paciente, self.profissional, self.leito, self.data_entrada])
