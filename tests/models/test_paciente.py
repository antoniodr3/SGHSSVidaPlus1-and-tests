


from PythonVidaPlus1.models.paciente import Paciente

def test_criar_paciente():
    paciente = Paciente("pac1", "João", 30, "Masculino", "99999-9999")
    assert paciente.nome == "João"
    assert paciente.idade == 30
    assert paciente.genero == "Masculino"
    assert paciente.contato == "99999-9999"

def test_validar_paciente_valido():
    paciente = Paciente("pac1", "João", 30, "Masculino", "99999-9999")
    assert paciente.validar() is True

def test_validar_paciente_invalido():
    paciente = Paciente("", "", None, "", "")
    assert paciente.validar() is False
