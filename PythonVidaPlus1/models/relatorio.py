


class Relatorio:
    def __init__(self, leitos, internacoes):
        self.leitos = leitos
        self.internacoes = internacoes

    def total_leitos(self):
        return len(self.leitos)

    def leitos_ocupados(self):
        return len([l for l in self.leitos if l.ocupado])

    def leitos_disponiveis(self):
        return len([l for l in self.leitos if not l.ocupado])

    def pacientes_internados(self):
        return [i.paciente for i in self.internacoes if not i.data_alta]

    def validar(self):
        return self.leitos is not None and self.internacoes is not None
