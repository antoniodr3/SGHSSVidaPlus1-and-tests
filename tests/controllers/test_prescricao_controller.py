


from PythonVidaPlus1.controllers.prescricao_controller import PrescricaoController

def test_criar_prescricao_controller():
    controller = PrescricaoController()
    prescricao = controller.criar_prescricao("Paracetamol", "500mg", "2x ao dia", "2025-12-10", "Dr. Carlos")
    assert prescricao.medicamento == "Paracetamol"
    assert prescricao.dosagem == "500mg"

def test_validar_prescricao_controller_valida():
    controller = PrescricaoController()
    prescricao = controller.criar_prescricao("Paracetamol", "500mg", "2x ao dia", "2025-12-10", "Dr. Carlos")
    assert controller.validar(prescricao) is True

def test_validar_prescricao_controller_invalida():
    controller = PrescricaoController()
    prescricao = controller.criar_prescricao("", "", "", "", "")
    assert controller.validar(prescricao) is False
