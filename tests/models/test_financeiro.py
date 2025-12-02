


from PythonVidaPlus1.models.financeiro import Financeiro

def test_registrar_transacao():
    fin = Financeiro()
    fin.registrar_transacao("Consulta", 200.0)
    assert fin.calcular_total() == 200.0
    assert len(fin.listar_transacoes()) == 1

def test_validar_financeiro():
    fin = Financeiro()
    assert fin.validar() is True
