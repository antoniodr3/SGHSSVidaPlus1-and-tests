


from PythonVidaPlus1.models.sistema import Sistema

class SistemaController:
    def criar_sistema(self, pacientes, profissionais, internacoes, relatorios, teleconsultas, financeiro, integracoes, governanca):
        return Sistema(pacientes, profissionais, internacoes, relatorios, teleconsultas, financeiro, integracoes, governanca)

    def validar(self, sistema: Sistema):
        return sistema.validar()

    def resumo(self, sistema: Sistema):
        return sistema.resumo()
