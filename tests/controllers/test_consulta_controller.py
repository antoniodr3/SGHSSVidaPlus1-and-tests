


from PythonVidaPlus1.controllers.consulta_controller import ConsultaController

def test_criar_consulta():
    controller = ConsultaController()
    consulta = controller.criar_consulta("Maria", "Dr. Carlos", "2025-12-01", "Dor de cabeça")
    assert consulta.paciente == "Maria"
    assert consulta.profissional == "Dr. Carlos"
    assert consulta.data == "2025-12-01"
    assert consulta.motivo == "Dor de cabeça"

def test_validar_consulta_valida():
    controller = ConsultaController()
    consulta = controller.criar_consulta("Maria", "Dr. Carlos", "2025-12-01", "Dor de cabeça")
    assert controller.validar(consulta) is True  # ✅ Corrigido para refletir o retorno esperado

def test_validar_consulta_invalida():
    controller = ConsultaController()
    consulta = controller.criar_consulta("", "", "", "")
    assert controller.validar(consulta) is False
