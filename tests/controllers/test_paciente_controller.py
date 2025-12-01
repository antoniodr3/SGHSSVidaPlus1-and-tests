


from PythonVidaPlus1.controllers.paciente_controller import PacienteController

def test_criar_paciente_controller():
    controller = PacienteController()
    paciente = controller.criar_paciente("pac1", "João", 30, "Masculino", "99999-9999")
    assert paciente.nome == "João"
    assert paciente.idade == 30

def test_validar_paciente_controller_valido():
    controller = PacienteController()
    paciente = controller.criar_paciente("pac1", "João", 30, "Masculino", "99999-9999")
    assert controller.validar(paciente) is True

def test_validar_paciente_controller_invalido():
    controller = PacienteController()
    paciente = controller.criar_paciente("", "", None, "", "")
    assert controller.validar(paciente) is False
