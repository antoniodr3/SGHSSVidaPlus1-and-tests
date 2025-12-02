


from PythonVidaPlus1.controllers.sistema_controller import SistemaController
from PythonVidaPlus1.models.financeiro import Financeiro
from PythonVidaPlus1.models.governanca import Governanca

def test_criar_sistema_controller():
    controller = SistemaController()
    financeiro = Financeiro()
    governanca = Governanca()
    sistema = controller.criar_sistema(["Paciente1"], ["Profissional1"], ["Internacao1"], ["Relatorio1"], ["Teleconsulta1"], financeiro, ["Integracao1"], governanca)
    assert sistema.validar() is True

def test_resumo_sistema_controller():
    controller = SistemaController()
    financeiro = Financeiro()
    governanca = Governanca()
    sistema = controller.criar_sistema(["Paciente1"], ["Profissional1"], ["Internacao1"], ["Relatorio1"], ["Teleconsulta1"], financeiro, ["Integracao1"], governanca)
    resumo = controller.resumo(sistema)
    assert resumo["pacientes"] == 1
    assert resumo["profissionais"] == 1
