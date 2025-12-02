


from PythonVidaPlus1.models.prontuario import Prontuario
from PythonVidaPlus1.models.consulta import Consulta
from PythonVidaPlus1.models.exame import Exame
from PythonVidaPlus1.models.paciente import Paciente
from PythonVidaPlus1.models.prescricao import Prescricao

def test_criar_prontuario():
    paciente = Paciente("p1", "João", 30, "Masculino", "99999-9999")
    prontuario = Prontuario(paciente)
    assert prontuario.paciente == paciente
    assert prontuario.listar_registros() == []

def test_adicionar_consulta():
    paciente = Paciente("p1", "João", 30, "Masculino", "99999-9999")
    consulta = Consulta("João", "Dr. Carlos", "2025-12-01", "Rotina")
    prontuario = Prontuario(paciente)
    prontuario.adicionar_registro(consulta)
    assert consulta in prontuario.listar_registros()

def test_adicionar_exame():
    paciente = Paciente("p1", "João", 30, "Masculino", "99999-9999")
    exame = Exame("João", "Dra. Ana", "Hemograma")
    prontuario = Prontuario(paciente)
    prontuario.adicionar_registro(exame)
    assert exame in prontuario.listar_registros()

def test_adicionar_prescricao():   # ✅ novo teste
    paciente = Paciente("p1", "João", 30, "Masculino", "99999-9999")
    prescricao = Prescricao("Paracetamol", "500mg", "2x ao dia", "2025-12-10", "Dr. Carlos")
    prontuario = Prontuario(paciente)
    prontuario.adicionar_registro(prescricao)
    assert prescricao in prontuario.listar_registros()
    assert prontuario.validar() is True

def test_validar_prontuario_valido():
    paciente = Paciente("p1", "João", 30, "Masculino", "99999-9999")
    consulta = Consulta("João", "Dr. Carlos", "2025-12-01", "Rotina")
    prontuario = Prontuario(paciente, [consulta])
    assert prontuario.validar() is True

def test_validar_prontuario_invalido():
    prontuario = Prontuario(None, [])
    assert prontuario.validar() is False

