


from PythonVidaPlus1.controllers.internacao_controller import InternacaoController
from PythonVidaPlus1.models.paciente import Paciente
from PythonVidaPlus1.models.profissional import Profissional
from PythonVidaPlus1.models.leito import Leito

def test_criar_internacao_controller():
    controller = InternacaoController()
    paciente = Paciente("p1", "João", 30, "Masculino", "99999-9999")
    profissional = Profissional("Dr. Ana", "Clínico Geral", "CRM123")
    leito = Leito("L1", "UTI")
    internacao = controller.criar_internacao(paciente, profissional, leito, "2025-12-01")
    assert internacao.leito.ocupado is True

def test_finalizar_internacao_controller():
    controller = InternacaoController()
    paciente = Paciente("p1", "João", 30, "Masculino", "99999-9999")
    profissional = Profissional("Dr. Ana", "Clínico Geral", "CRM123")
    leito = Leito("L1", "UTI")
    internacao = controller.criar_internacao(paciente, profissional, leito, "2025-12-01")
    controller.finalizar_internacao(internacao, "2025-12-10")
    assert internacao.data_alta == "2025-12-10"
    assert leito.ocupado is False

def test_validar_internacao_controller():
    controller = InternacaoController()
    paciente = Paciente("p1", "João", 30, "Masculino", "99999-9999")
    profissional = Profissional("Dr. Ana", "Clínico Geral", "CRM123")
    leito = Leito("L1", "UTI")
    internacao = controller.criar_internacao(paciente, profissional, leito, "2025-12-01")
    assert controller.validar(internacao) is True
