


from PythonVidaPlus1.models.teleconsulta import Teleconsulta
from PythonVidaPlus1.models.prescricao import Prescricao

def test_criar_teleconsulta():
    teleconsulta = Teleconsulta("João", "Dr. Carlos", "2025-12-05", "Rotina", "https://link.com")
    assert teleconsulta.paciente == "João"
    assert teleconsulta.profissional == "Dr. Carlos"
    assert teleconsulta.link == "https://link.com"

def test_resumo_teleconsulta():
    teleconsulta = Teleconsulta("João", "Dr. Carlos", "2025-12-05", "Rotina", "https://link.com")
    resumo = teleconsulta.resumo()
    assert "João" in resumo
    assert "Dr. Carlos" in resumo
    assert "https://link.com" in resumo

def test_validar_teleconsulta_valida():
    teleconsulta = Teleconsulta("João", "Dr. Carlos", "2025-12-05", "Rotina", "https://link.com")
    assert teleconsulta.validar() is True

def test_validar_teleconsulta_invalida():
    teleconsulta = Teleconsulta("", "", "", "", "")
    assert teleconsulta.validar() is False

def test_teleconsulta_com_prescricao():
    prescricao = Prescricao("Paracetamol", "500mg", "2x ao dia", "2025-12-10", "Dr. Carlos")
    teleconsulta = Teleconsulta("João", "Dr. Carlos", "2025-12-05", "Rotina", "https://link.com", prescricao)
    assert teleconsulta.prescricao == prescricao
