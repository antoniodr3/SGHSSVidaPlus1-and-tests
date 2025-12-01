


from PythonVidaPlus1.models.relatorio_financeiro import RelatorioFinanceiro

def test_adicionar_entrada_e_saida():
    relatorio = RelatorioFinanceiro()
    relatorio.adicionar_entrada(1000)
    relatorio.adicionar_saida(200)
    assert relatorio.calcular_saldo() == 800

def test_relatorio_vazio():
    relatorio = RelatorioFinanceiro()
    assert relatorio.calcular_saldo() == 0

def test_validar_relatorio():
    relatorio = RelatorioFinanceiro()
    assert relatorio.validar() is True
