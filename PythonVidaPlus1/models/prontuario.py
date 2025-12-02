


class Prontuario:
    def __init__(self, paciente, registros=None):
        self.paciente = paciente
        self.registros = registros if registros else []

    def adicionar_registro(self, registro):
        self.registros.append(registro)

    def listar_registros(self):
        return self.registros

    def validar(self):
        # Precisa ter paciente e pelo menos um registro
        return bool(self.paciente and self.registros)
