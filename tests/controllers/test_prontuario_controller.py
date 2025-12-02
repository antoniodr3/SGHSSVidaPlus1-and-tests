


from PythonVidaPlus1.controllers.prontuario_controller import ProntuarioController
from PythonVidaPlus1.models.paciente import Paciente
from PythonVidaPlus1.models.consulta import Consulta

def test_criar_prontuario_controller():
    controller = ProntuarioController()
    paciente = Paciente("p1", "João", 30, "Masculino", "99999-9999")
    prontuario = controller.criar_prontuario(paciente)
    assert prontuario.paciente == paciente

def test_adicionar_registro_controller():
    controller = ProntuarioController()
    paciente = Paciente("p1", "João", 30, "Masculino", "99999-9999")
    consulta = Consulta("João", "Dr. Carlos", "2025-12-01", "Rotina")
    prontuario = controller.criar_prontuario(paciente)
    controller.adicionar_registro(prontuario, consulta)
    assert consulta in prontuario.listar_registros()

def test_validar_prontuario_controller():
    controller = ProntuarioController()
    paciente = Paciente("p1", "João", 30, "Masculino", "99999-9999")
    consulta = Consulta("João", "Dr. Carlos", "2025-12-01", "Rotina")
    prontuario = controller.criar_prontuario(paciente)
    controller.adicionar_registro(prontuario, consulta)
    assert controller.validar(prontuario) is True
