


class Agendamento:
    def __init__(self, paciente, profissional, consulta):
        self.paciente = paciente
        self.profissional = profissional
        self.consulta = consulta

    def validar(self):
        # Validação simples: todos os objetos precisam existir
        return all([self.paciente, self.profissional, self.consulta])