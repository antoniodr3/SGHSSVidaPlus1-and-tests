


from PythonVidaPlus1.controllers.relatorio_financeiro_controller import RelatorioFinanceiroController


def test_relatorio_financeiro_controller():
    controller = RelatorioFinanceiroController()
    relatorio = controller.criar_relatorio()
    controller.adicionar_entrada(relatorio, 500)
    controller.adicionar_saida(relatorio, 200)
    assert controller.calcular_saldo(relatorio) == 300
    assert controller.validar(relatorio) is True
