


from PythonVidaPlus1.controllers.profissional_controller import ProfissionalController

def test_criar_profissional():
    controller = ProfissionalController()
    prof = controller.criar_profissional("Dr. Pedro", "Cardiologia", "CRM12345")
    assert prof.nome == "Dr. Pedro"
    assert prof.especialidade == "Cardiologia"
    assert prof.registro == "CRM12345"

def test_validar_profissional_valido():
    controller = ProfissionalController()
    prof = controller.criar_profissional("Dr. Pedro", "Cardiologia", "CRM12345")
    assert controller.validar(prof) is True

def test_validar_profissional_invalido():
    controller = ProfissionalController()
    prof = controller.criar_profissional("", "", "")
    assert controller.validar(prof) is False
