


from PythonVidaPlus1.models.internacao import Internacao
from PythonVidaPlus1.models.paciente import Paciente
from PythonVidaPlus1.models.profissional import Profissional
from PythonVidaPlus1.models.leito import Leito

def test_criar_internacao():
    paciente = Paciente("p1", "João", 30, "Masculino", "99999-9999")
    profissional = Profissional("Dr. Ana", "Clínico Geral", "CRM123")
    leito = Leito("L1", "UTI")
    internacao = Internacao(paciente, profissional, leito, "2025-12-01")
    assert internacao.paciente == paciente
    assert internacao.leito == leito
    assert internacao.data_entrada == "2025-12-01"

def test_finalizar_internacao():
    paciente = Paciente("p1", "João", 30, "Masculino", "99999-9999")
    profissional = Profissional("Dr. Ana", "Clínico Geral", "CRM123")
    leito = Leito("L1", "UTI")
    internacao = Internacao(paciente, profissional, leito, "2025-12-01")
    internacao.finalizar("2025-12-10")
    assert internacao.data_alta == "2025-12-10"
    assert leito.ocupado is False

def test_validar_internacao_invalida():
    internacao = Internacao(None, None, None, "")
    assert internacao.validar() is False
