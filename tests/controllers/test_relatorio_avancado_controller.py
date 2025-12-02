


from PythonVidaPlus1.controllers.relatorio_avancado_controller import RelatorioAvancadoController
from PythonVidaPlus1.models.financeiro import Financeiro

def test_gerar_relatorio_avancado_controller():
    controller = RelatorioAvancadoController()
    financeiro = Financeiro()
    relatorio = controller.gerar_relatorio([], [], [], financeiro)
    assert relatorio.validar() is True

def test_validar_relatorio_avancado_controller():
    controller = RelatorioAvancadoController()
    financeiro = Financeiro()
    relatorio = controller.gerar_relatorio([], [], [], financeiro)
    assert controller.validar(relatorio) is True
