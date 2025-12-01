


from PythonVidaPlus1.controllers.agendamento_controller import AgendamentoController
from PythonVidaPlus1.models.paciente import Paciente
from PythonVidaPlus1.models.profissional import Profissional
from PythonVidaPlus1.models.consulta import Consulta

def test_criar_agendamento_controller():
    controller = AgendamentoController()
    paciente = Paciente("p1", "João", 30, "Masculino", "99999-9999")
    profissional = Profissional("pr1", "Dra. Ana", "CRM123")
    consulta = Consulta("João", "Dra. Ana", "2025-12-01 10:00", "Rotina")

    agendamento = controller.criar_agendamento(paciente, profissional, consulta)
    assert agendamento.paciente == paciente
    assert agendamento.profissional == profissional
    assert agendamento.consulta == consulta

def test_validar_agendamento_controller_valido():
    controller = AgendamentoController()
    paciente = Paciente("p1", "João", 30, "Masculino", "99999-9999")
    profissional = Profissional("pr1", "Dra. Ana", "CRM123")
    consulta = Consulta("João", "Dra. Ana", "2025-12-01 10:00", "Rotina")

    agendamento = controller.criar_agendamento(paciente, profissional, consulta)
    assert controller.validar(agendamento) is True

def test_validar_agendamento_controller_invalido():
    controller = AgendamentoController()
    agendamento = controller.criar_agendamento(None, None, None)
    assert controller.validar(agendamento) is False
