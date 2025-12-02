


from PythonVidaPlus1.controllers.financeiro_controller import FinanceiroController

def test_registrar_transacao_controller():
    controller = FinanceiroController()
    controller.registrar_transacao("Exame", 150.0)
    assert controller.calcular_total() == 150.0

def test_listar_transacoes_controller():
    controller = FinanceiroController()
    controller.registrar_transacao("Internação", 500.0)
    transacoes = controller.listar_transacoes()
    assert any(t["descricao"] == "Internação" for t in transacoes)
