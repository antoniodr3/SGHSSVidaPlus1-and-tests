


from PythonVidaPlus1.models.relatorio_financeiro import RelatorioFinanceiro

class RelatorioFinanceiroController:
    def criar_relatorio(self):
        return RelatorioFinanceiro()

    def adicionar_entrada(self, relatorio: RelatorioFinanceiro, valor):
        relatorio.adicionar_entrada(valor)
        return relatorio

    def adicionar_saida(self, relatorio: RelatorioFinanceiro, valor):
        relatorio.adicionar_saida(valor)
        return relatorio

    def calcular_saldo(self, relatorio: RelatorioFinanceiro):
        return relatorio.calcular_saldo()

    def validar(self, relatorio: RelatorioFinanceiro):
        return relatorio.validar()


