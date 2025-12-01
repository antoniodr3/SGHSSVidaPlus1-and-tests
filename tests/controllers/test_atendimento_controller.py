


from PythonVidaPlus1.controllers.atendimento_controller import AtendimentoController
from PythonVidaPlus1.models.paciente import Paciente
from PythonVidaPlus1.models.profissional import Profissional
from PythonVidaPlus1.models.consulta import Consulta
from PythonVidaPlus1.models.exame import Exame

def test_criar_atendimento_controller_com_consulta():
    controller = AtendimentoController()
    paciente = Paciente("p1", "João", 30, "Masculino", "99999-9999")
    profissional = Profissional("pr1", "Dra. Ana", "CRM123")
    consulta = Consulta("João", "Dra. Ana", "2025-12-01 10:00", "Rotina")

    atendimento = controller.criar_atendimento(paciente, profissional, consulta=consulta)
    assert controller.validar(atendimento) is True

def test_criar_atendimento_controller_com_exame():
    controller = AtendimentoController()
    paciente = Paciente("p2", "Maria", 25, "Feminino", "88888-8888")
    profissional = Profissional("pr2", "Dr. Carlos", "CRM456")
    exame = Exame("Maria", "Hemograma", "2025-12-02 09:00")

    atendimento = controller.criar_atendimento(paciente, profissional, exame=exame)
    assert controller.validar(atendimento) is True

def test_atendimento_controller_invalido():
    controller = AtendimentoController()
    atendimento = controller.criar_atendimento(None, None, None, None)
    assert controller.validar(atendimento) is False
