


class Atendimento:
    def __init__(self, paciente, profissional, consulta=None, exame=None):
        self.paciente = paciente
        self.profissional = profissional
        self.consulta = consulta
        self.exame = exame

    def validar(self):
        # Validação simples: paciente e profissional precisam existir
        if not self.paciente or not self.profissional:
            return False

        # Pelo menos uma ação (consulta ou exame) precisa existir
        if not self.consulta and not self.exame:
            return False

        return True
