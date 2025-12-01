


from PythonVidaPlus1.models.atendimento import Atendimento
from PythonVidaPlus1.models.paciente import Paciente
from PythonVidaPlus1.models.profissional import Profissional
from PythonVidaPlus1.models.consulta import Consulta
from PythonVidaPlus1.models.exame import Exame

def test_criar_atendimento_com_consulta():
    paciente = Paciente("p1", "João", 30, "Masculino", "99999-9999")
    profissional = Profissional("pr1", "Dra. Ana", "CRM123")
    consulta = Consulta("João", "Dra. Ana", "2025-12-01 10:00", "Rotina")

    atendimento = Atendimento(paciente, profissional, consulta=consulta)
    assert atendimento.paciente == paciente
    assert atendimento.profissional == profissional
    assert atendimento.consulta == consulta
    assert atendimento.validar() is True

def test_criar_atendimento_com_exame():
    paciente = Paciente("p2", "Maria", 25, "Feminino", "88888-8888")
    profissional = Profissional("pr2", "Dr. Carlos", "CRM456")
    exame = Exame("Maria", "Hemograma", "2025-12-02 09:00")

    atendimento = Atendimento(paciente, profissional, exame=exame)
    assert atendimento.exame == exame
    assert atendimento.validar() is True

def test_atendimento_invalido_sem_paciente_profissional():
    atendimento = Atendimento(None, None, None, None)
    assert atendimento.validar() is False
