


from PythonVidaPlus1.models.agendamento import Agendamento
from PythonVidaPlus1.models.paciente import Paciente
from PythonVidaPlus1.models.profissional import Profissional
from PythonVidaPlus1.models.consulta import Consulta

def test_criar_agendamento():
    paciente = Paciente("p1", "João", 30, "Masculino", "99999-9999")
    profissional = Profissional("pr1", "Dra. Ana", "CRM123")
    consulta = Consulta("João", "Dra. Ana", "2025-12-01 10:00", "Rotina")

    agendamento = Agendamento(paciente, profissional, consulta)
    assert agendamento.paciente == paciente
    assert agendamento.profissional == profissional
    assert agendamento.consulta == consulta

def test_validar_agendamento_valido():
    paciente = Paciente("p1", "João", 30, "Masculino", "99999-9999")
    profissional = Profissional("pr1", "Dra. Ana", "CRM123")
    consulta = Consulta("João", "Dra. Ana", "2025-12-01 10:00", "Rotina")

    agendamento = Agendamento(paciente, profissional, consulta)
    assert agendamento.validar() is True

def test_validar_agendamento_invalido():
    agendamento = Agendamento(None, None, None)
    assert agendamento.validar() is False
