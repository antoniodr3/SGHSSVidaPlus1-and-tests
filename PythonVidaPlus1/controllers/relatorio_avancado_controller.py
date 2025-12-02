


from PythonVidaPlus1.models.relatorio_avancado import RelatorioAvancado

class RelatorioAvancadoController:
    def gerar_relatorio(self, unidades, internacoes, consultas, financeiro):
        return RelatorioAvancado(unidades, internacoes, consultas, financeiro)

    def validar(self, relatorio: RelatorioAvancado):
        return relatorio.validar()
