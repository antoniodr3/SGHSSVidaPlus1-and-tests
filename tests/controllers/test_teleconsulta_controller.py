


from PythonVidaPlus1.controllers.teleconsulta_controller import TeleconsultaController
from PythonVidaPlus1.models.prescricao import Prescricao

def test_criar_teleconsulta_controller():
    controller = TeleconsultaController()
    teleconsulta = controller.criar_teleconsulta("João", "Dr. Carlos", "2025-12-05", "Rotina", "https://link.com")
    assert teleconsulta.link == "https://link.com"

def test_validar_teleconsulta_controller_valida():
    controller = TeleconsultaController()
    teleconsulta = controller.criar_teleconsulta("João", "Dr. Carlos", "2025-12-05", "Rotina", "https://link.com")
    assert controller.validar(teleconsulta) is True

def test_validar_teleconsulta_controller_invalida():
    controller = TeleconsultaController()
    teleconsulta = controller.criar_teleconsulta("", "", "", "", "")
    assert controller.validar(teleconsulta) is False

def test_teleconsulta_controller_com_prescricao():
    controller = TeleconsultaController()
    prescricao = Prescricao("Ibuprofeno", "400mg", "3x ao dia", "2025-12-15", "Dra. Ana")
    teleconsulta = controller.criar_teleconsulta("Maria", "Dra. Ana", "2025-12-06", "Dor de cabeça", "https://link.com", prescricao)
    assert teleconsulta.prescricao == prescricao
