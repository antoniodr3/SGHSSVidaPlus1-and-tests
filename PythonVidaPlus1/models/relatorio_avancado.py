


class RelatorioAvancado:
    def __init__(self, unidades, internacoes, consultas, financeiro):
        self.unidades = unidades
        self.internacoes = internacoes
        self.consultas = consultas
        self.financeiro = financeiro

    def taxa_ocupacao_media(self):
        total_leitos = sum(len(u.leitos) for u in self.unidades)
        ocupados = sum(len([l for l in u.leitos if l.ocupado]) for u in self.unidades)
        return (ocupados / total_leitos) * 100 if total_leitos > 0 else 0

    def tempo_medio_internacao(self):
        duracoes = []
        for i in self.internacoes:
            if i.data_alta and i.data_internacao:
                dias = (i.data_alta - i.data_internacao).days
                duracoes.append(dias)
        return sum(duracoes) / len(duracoes) if duracoes else 0

    def total_consultas(self):
        return len(self.consultas)

    def custos_totais(self):
        return self.financeiro.calcular_total()

    def validar(self):
        return all([self.unidades is not None, self.internacoes is not None, self.consultas is not None, self.financeiro is not None])
