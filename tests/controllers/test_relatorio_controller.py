


from PythonVidaPlus1.controllers.relatorio_controller import RelatorioController
from PythonVidaPlus1.models.leito import Leito

def test_gerar_relatorio_controller():
    controller = RelatorioController()
    leito = Leito("L1", "UTI")
    relatorio = controller.gerar_relatorio([leito], [])
    assert relatorio.total_leitos() == 1

def test_validar_relatorio_controller():
    controller = RelatorioController()
    relatorio = controller.gerar_relatorio([], [])
    assert controller.validar(relatorio) is True
