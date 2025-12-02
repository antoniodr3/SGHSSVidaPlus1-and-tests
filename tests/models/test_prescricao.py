


from PythonVidaPlus1.models.prescricao import Prescricao

def test_criar_prescricao():
    prescricao = Prescricao("Paracetamol", "500mg", "2x ao dia", "2025-12-10", "Dr. Carlos")
    assert prescricao.medicamento == "Paracetamol"
    assert prescricao.dosagem == "500mg"
    assert prescricao.frequencia == "2x ao dia"
    assert prescricao.validade == "2025-12-10"
    assert prescricao.profissional == "Dr. Carlos"

def test_resumo_prescricao():
    prescricao = Prescricao("Paracetamol", "500mg", "2x ao dia", "2025-12-10", "Dr. Carlos")
    resumo = prescricao.resumo()
    assert "Paracetamol" in resumo
    assert "500mg" in resumo
    assert "2x ao dia" in resumo
    assert "2025-12-10" in resumo
    assert "Dr. Carlos" in resumo

def test_validar_prescricao_valida():
    prescricao = Prescricao("Paracetamol", "500mg", "2x ao dia", "2025-12-10", "Dr. Carlos")
    assert prescricao.validar() is True

def test_validar_prescricao_invalida():
    prescricao = Prescricao("", "", "", "", "")
    assert prescricao.validar() is False
