


from PythonVidaPlus1.controllers.unidade_controller import UnidadeController
from PythonVidaPlus1.models.leito import Leito
from PythonVidaPlus1.models.internacao import Internacao
from PythonVidaPlus1.models.paciente import Paciente
from PythonVidaPlus1.models.profissional import Profissional

def test_criar_unidade_controller():
    controller = UnidadeController()
    unidade = controller.criar_unidade("U1", "Hospital Central", "Rua A, 123")
    assert unidade.nome == "Hospital Central"

def test_adicionar_leito_controller():
    controller = UnidadeController()
    unidade = controller.criar_unidade("U1", "Hospital Central", "Rua A, 123")
    leito = Leito("L1", "UTI")
    controller.adicionar_leito(unidade, leito)
    assert leito in unidade.listar_leitos()

def test_adicionar_internacao_controller():
    controller = UnidadeController()
    unidade = controller.criar_unidade("U1", "Hospital Central", "Rua A, 123")
    paciente = Paciente("p1", "João", 30, "Masculino", "99999-9999")
    profissional = Profissional("Dr. Ana", "Clínico Geral", "CRM123")
    leito = Leito("L1", "UTI")
    internacao = Internacao(paciente, profissional, leito, "2025-12-01")
    controller.adicionar_internacao(unidade, internacao)
    assert internacao in unidade.listar_internacoes()
