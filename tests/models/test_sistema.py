


from PythonVidaPlus1.models.sistema import Sistema
from PythonVidaPlus1.models.financeiro import Financeiro
from PythonVidaPlus1.models.governanca import Governanca

def test_criar_sistema_valido():
    financeiro = Financeiro()
    governanca = Governanca()
    sistema = Sistema(["Paciente1"], ["Profissional1"], ["Internacao1"], ["Relatorio1"], ["Teleconsulta1"], financeiro, ["Integracao1"], governanca)
    assert sistema.validar() is True

def test_resumo_sistema():
    financeiro = Financeiro()
    governanca = Governanca()
    sistema = Sistema(["Paciente1"], ["Profissional1"], ["Internacao1"], ["Relatorio1"], ["Teleconsulta1"], financeiro, ["Integracao1"], governanca)
    resumo = sistema.resumo()
    assert resumo["pacientes"] == 1
    assert resumo["profissionais"] == 1
    assert resumo["internacoes"] == 1
