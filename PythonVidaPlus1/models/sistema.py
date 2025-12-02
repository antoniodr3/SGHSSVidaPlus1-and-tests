


class Sistema:
    def __init__(self, pacientes, profissionais, internacoes, relatorios, teleconsultas, financeiro, integracoes, governanca):
        self.pacientes = pacientes
        self.profissionais = profissionais
        self.internacoes = internacoes
        self.relatorios = relatorios
        self.teleconsultas = teleconsultas
        self.financeiro = financeiro
        self.integracoes = integracoes
        self.governanca = governanca

    def resumo(self):
        return {
            "pacientes": len(self.pacientes),
            "profissionais": len(self.profissionais),
            "internacoes": len(self.internacoes),
            "teleconsultas": len(self.teleconsultas),
            "transacoes_financeiras": len(self.financeiro.transacoes),
            "integracoes": len(self.integracoes),
            "backups": len(self.governanca.backups)
        }

    def validar(self):
        return all([
            self.pacientes is not None,
            self.profissionais is not None,
            self.internacoes is not None,
            self.relatorios is not None,
            self.teleconsultas is not None,
            self.financeiro is not None,
            self.integracoes is not None,
            self.governanca is not None
        ])
