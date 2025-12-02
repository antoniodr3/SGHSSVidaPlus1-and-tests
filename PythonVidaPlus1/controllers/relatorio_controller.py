


from PythonVidaPlus1.models.relatorio import Relatorio

class RelatorioController:
    def gerar_relatorio(self, leitos, internacoes):
        return Relatorio(leitos, internacoes)

    def validar(self, relatorio: Relatorio):
        return relatorio.validar()
